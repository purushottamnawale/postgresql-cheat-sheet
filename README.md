# PostgreSQL Cheat Sheet

## Commands in Shell/Bash 
##### Switch to user 'postgres'
```
sudo -i -u postgres
```
##### Switch to user 'postgres' and start PostgreSQL command-line client
```
sudo -u postgres psql
```

##### Check Status 
```
sudo systemctl status postgresql
```

#### Check PostgreSQL Version
```
psql --version
```


## Commands In psql
##### Change Database
```
\c <database_name>
```

##### List all Database
```
\l
```
```
\list
```

##### Note: Captial Case is optional
##### Create Database 
```
CREATE DATABASE <database_name>;
```

##### Create a user
```
CREATE USER <user> WITH PASSWORD 'password';
```

#### Grant all permissions
```
GRANT ALL PRIVILEGES ON DATABASE "testdb" to <user>;
```

#### Delete a Database
```
DROP DATABASE <database_name>;
```


# Join
#### Create a Table
```
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);


CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);
```

#### Insert Data into the table
```
INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');


INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
```

#### Inner Join (Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
INNER JOIN basket_b
    ON fruit_a = fruit_b;
```
```
 a | fruit_a | b | fruit_b 
---+---------+---+---------
 1 | Apple   | 2 | Apple
 2 | Orange  | 1 | Orange
(2 rows)
```


#### Left Join (Left Table + Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b 
   ON fruit_a = fruit_b;
```

```
 a | fruit_a  | b | fruit_b 
---+----------+---+---------
 1 | Apple    | 2 | Apple
 2 | Orange   | 1 | Orange
 3 | Banana   |   | 
 4 | Cucumber |   | 
(4 rows)
```

#### Left Join (Left Table - Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b 
    ON fruit_a = fruit_b
WHERE b IS NULL;
```
```
 a | fruit_a  | b | fruit_b 
---+----------+---+---------
 3 | Banana   |   | 
 4 | Cucumber |   | 
(2 rows)

```

#### Right Join (Right Table + Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b 
   ON fruit_a = fruit_b;
```
```
 a | fruit_a | b |  fruit_b   
---+---------+---+------------
 2 | Orange  | 1 | Orange
 1 | Apple   | 2 | Apple
   |         | 3 | Watermelon
   |         | 4 | Pear
(4 rows)
```

#### Right Join (Right Table - Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b 
    ON fruit_a = fruit_b
WHERE a IS NULL;
```
```
 a | fruit_a | b |  fruit_b   
---+---------+---+------------
   |         | 3 | Watermelon
   |         | 4 | Pear
(2 rows)
```

#### Full Outer Join (Left Table + Right Table = Union)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL OUTER JOIN basket_b 
    ON fruit_a = fruit_b;
```
```
 a | fruit_a  | b |  fruit_b   
---+----------+---+------------
 1 | Apple    | 2 | Apple
 2 | Orange   | 1 | Orange
 3 | Banana   |   | 
 4 | Cucumber |   | 
   |          | 3 | Watermelon
   |          | 4 | Pear
(6 rows)
```

#### Full Outer Join (Left Table + Right Table - Intersection)
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL JOIN basket_b 
   ON fruit_a = fruit_b
WHERE a IS NULL OR b IS NULL;
```
```
 a | fruit_a  | b |  fruit_b   
---+----------+---+------------
 3 | Banana   |   | 
 4 | Cucumber |   | 
   |          | 3 | Watermelon
   |          | 4 | Pear
(4 rows)
```
More on Join:  
https://www.postgresql.org/docs/16/queries-table-expressions.html
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/

# Update
#### Create a Table and Insert Data
```
CREATE TABLE courses(
	course_id serial primary key,
	course_name VARCHAR(255) NOT NULL,
	description VARCHAR(500),
	published_date date
);

INSERT INTO 
	courses(course_name, description, published_date)
VALUES
	('PostgreSQL for Developers','A complete PostgreSQL for Developers','2020-07-13'),
	('PostgreSQL Admininstration','A PostgreSQL Guide for DBA',NULL),
	('PostgreSQL High Performance',NULL,NULL),
	('PostgreSQL Bootcamp','Learn PostgreSQL via Bootcamp','2013-07-11'),
	('Mastering PostgreSQL','Mastering PostgreSQL in 21 Days','2012-06-30');

```
```
CREATE TABLE  
INSERT 0 5
```
```
SELECT * FROM courses;
```
```
 course_id |         course_name         |             description              | published_date 
-----------+-----------------------------+--------------------------------------+----------------
         1 | PostgreSQL for Developers   | A complete PostgreSQL for Developers | 2020-07-13
         2 | PostgreSQL Admininstration  | A PostgreSQL Guide for DBA           | 
         3 | PostgreSQL High Performance |                                      | 
         4 | PostgreSQL Bootcamp         | Learn PostgreSQL via Bootcamp        | 2013-07-11
         5 | Mastering PostgreSQL        | Mastering PostgreSQL in 21 Days      | 2012-06-30
(5 rows)
```
```
UPDATE courses
SET published_date = '2020-08-01' 
WHERE course_id = 3;
```

```
UPDATE 1
```
```
 course_id |         course_name         | description | published_date 
-----------+-----------------------------+-------------+----------------
         3 | PostgreSQL High Performance |             | 2020-08-01
(1 row)
```

```
UPDATE courses
SET published_date = '2020-07-01'
WHERE course_id = 2
RETURNING *;
```
```
 course_id |        course_name         |        description         | published_date 
-----------+----------------------------+----------------------------+----------------
         2 | PostgreSQL Admininstration | A PostgreSQL Guide for DBA | 2020-07-01
(1 row)

UPDATE 1
```

More on Update:  
https://www.postgresql.org/docs/current/sql-update.html

More on Join:
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/