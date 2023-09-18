# PostgreSQL Cheat Sheet

## Commands in Shell/Bash 
##### Switch to user 'postgres'
```
sudo -u postgres
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

