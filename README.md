# SQL Cheat Sheet

## Commands in Shell/Bash 
##### Switch to user 'postgres'
```bash
sudo -i -u postgres
```
##### Switch to user 'postgres' and start PostgreSQL command-line client
Linux
```bash
sudo -u postgres psql
```
Windows
```bash
psql -U postgres
```

##### Check Status 
```bash
sudo systemctl status postgresql
```

#### Check PostgreSQL Version Both Windows and Linux
```bash
psql --version
postgres --version
```

```sql
SELECT version();
```


## Commands In psql
##### Shift to a Database or Change Database
```bash
\c <database_name>
```

##### List all Database
```bash
\l
```
or
```bash
\list
```

##### Note: Captial Case is optional
##### Create Database 
```sql
CREATE DATABASE <database_name>;
```

##### Create a user
```sql
CREATE USER <user> WITH PASSWORD 'password';
```

#### Grant all permissions
```sql
GRANT ALL PRIVILEGES ON DATABASE "testdb" to <user>;
```

#### Delete a Database
```sql
DROP DATABASE <database_name>;
```


#### PG DUMP
###### Windows
https://stackoverflow.com/a/76345277/25405144