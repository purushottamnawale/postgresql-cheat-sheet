import os
import re
import sys
from datetime import datetime

import django
import pandas as pd
import pytz
from django.db import connections

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_name.settings")
django.setup()

TIME_ZONE = "Asia/Kolkata"
date_time = datetime.now(pytz.timezone(TIME_ZONE))


def extract_table_name(query):
    pattern = re.compile(r"from\s+(\w+)", re.IGNORECASE)
    match = pattern.search(query)
    if match:
        return match.group(1)


def get_delete_query(cursor, exception):
    table_name_pattern = r' on table "([^"]+)"\nDETAIL:'
    table_name = re.search(table_name_pattern, exception).group(1)
    key_value_pattern = r"Key \([^)]+\)=\((\d+)\)"
    key_value = re.search(key_value_pattern, exception).group(1)

    cursor.execute(f"SELECT conname, a.attname AS column_name FROM pg_constraint AS c JOIN pg_attribute AS a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid WHERE c.conrelid = '{table_name}'::regclass;")
    foreign_keys = cursor.fetchall()

    for fk in foreign_keys:
        if fk[0] in exception:
            column_name = fk[1]
            break

    return table_name, column_name, key_value


def print_data(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    print(df)


def recursive_delete(cursor, table_name="", column_name="", value="", query=""):
    if query == "":
        query = f"""DELETE FROM {table_name} WHERE "{column_name}" = {value};"""
        print_data(cursor, f"""SELECT * FROM {table_name} WHERE "{column_name}" = {value};""")
        confirm = input(f"Are you sure you want execute query : {query} (y/n): ")
    else:
        confirm = "y"
        table_name = extract_table_name(query)

    flag = True
    while flag:
        try:
            if confirm == "y":
                cursor.execute(query)
                print(query + " executed successfully")
                flag = False
            else:
                return
        except Exception as e:
            exception = str(e)
            if "foreign key constraint" in exception:
                child_table_name, constraint_name, key_value = get_delete_query(cursor, exception)
                recursive_delete(cursor, child_table_name, constraint_name, key_value)


if __name__ == "__main__":
    cursor = connections["default"].cursor()
    query = input("Please Type Delete Query: ")
    if query:
        recursive_delete(query=query, cursor=cursor)
    else:
        recursive_delete("tbl_source_mst", "id", 77, cursor=cursor)
