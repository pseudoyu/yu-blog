---
title: "PostgreSQL Basics and Practice"
date: 2022-09-05T23:30:46+08:00
draft: false
tags: ["database", "postgres", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Preface

Recently, I've been thinking about organizing and summarizing the technical points and tools commonly used in my work. On one hand, this helps me review these knowledge points and deepen my memory of their usage. On the other hand, it can serve as a reference for future use.

Currently, I'm planning to cover several core areas including databases, CI/CD (GitHub Actions + GitLab CI), containers (Docker + k8s), operations (Ansible, etc.), as well as some summaries of language features, practical Git techniques, and Shell scripting tips. Since I've only encountered many of these topics at work and done some extended learning on my own, they may not fully align with specific enterprise practices (mostly based on my own experiences and understanding). I hope this can be helpful.

This article is the PostgreSQL part of the database series. I've previously summarized MySQL, which you can refer to in "MySQL Basic Knowledge and Related Operations".

## Overview of Data and Databases

### Data

Fundamentally, data is a type of fact or observed result, a logical summary of objective matters, and a form and carrier of information. People have been managing data since ancient times (even before the concept existed), initially through manual management, then gradually through file systems (like libraries, managing different information by categories), and finally, with the development of computer technology, forming the more convenient and efficient mode of database management.

### Database

A database is a repository that organizes, stores, and manages data according to a certain data structure. Its main characteristics are:

- Structured
- Shareable
- Low redundancy
- High independence
- Easy to expand

It's easy to understand that data organized according to different relationships/structures have different characteristics and are suitable for different application scenarios. Currently, there are mainly three types: hierarchical databases, network databases, and relational databases. PostgreSQL, which we will focus on, is a relational database.

### Database Management System (DBMS)

A Database Management System (DBMS) is a system that performs various operations on databases. It has core functions such as establishing and maintaining databases, organizing and managing data storage, controlling databases, defining data, manipulating data, and managing communication between data. Different database management systems handle databases and data differently, and the way data is presented also varies. It often requires choosing an appropriate database management system based on factors such as data scale and business requirements. For example, in situations with massive data and high-concurrency data read/write operations, the performance of relational databases can deteriorate significantly.

## Relational Database Management System (RDBMS)

### Main Characteristics

Relational databases primarily present data in the form of data tables, with each row representing a record and each column corresponding to the data field of the record name. Many rows and columns form a single table, and several single tables form a database. Users/systems query the database through SQL (Structured Query Language).

Some relational database operations have transactional properties, namely the ACID rules:

- Atomicity
- Consistency
- Isolation
- Durability

Atomicity means that a series of transaction operations must either all complete or all fail; there is no situation where only part is completed. For example, in a bank transfer scenario, after the transfer occurs, the sender's balance decreases, but if a database operation error occurs and the receiver's balance does not increase, it would cause serious problems.

Consistency means that after a transaction is completed, the data in the entire database is consistent; there should be no situation where the same data is out of sync within the database.

Isolation means that different transactions should run independently and without interference. Of course, this sacrifices some efficiency but provides better guarantees for data accuracy.

Durability means that when a transaction is completed, its changes to the database and its effects on the system are permanent.

### Data Integrity

Data integrity is a very important requirement and property of databases, referring to the consistency and reliability of data stored in the database. It is mainly divided into four types:

- Entity integrity
- Domain integrity
- Referential integrity
- User-defined integrity

Entity integrity requires that each data table has a unique identifier, and the primary key field in each table cannot be empty or duplicate, mainly meaning that the data in the table can be uniquely distinguished.

Domain integrity is to make some additional restrictions on the columns in the table, such as restricting data types, check constraints, setting default values, whether to allow null values, and value range.

```sql
--- Constraining field uniqueness when creating a table
CREATE TABLE person (
    id INT NOT NULL auto_increment PRIMARY KEY,
    name VARCHAR(30),
    id_number VARCHAR(18) UNIQUE
);
```

Referential integrity means that the database does not allow referencing non-existent entities. Tables in the database often have some associations with other tables, and referential integrity can be ensured through foreign key constraints.

User-defined integrity is to make some semantic restrictions on data according to specific application scenarios and involved data, such as balance cannot be negative, etc. It is generally constrained and limited by setting rules, stored procedures, and triggers.

### Mainstream RDBMS

Currently, the mainstream relational database management systems include:

- SQL Server
- Sybase
- DB2
- Oracle
- MySQL
- PostgreSQL

Oracle, MySQL, and PostgreSQL are more commonly used by enterprises and individuals. Next, we will use PostgreSQL as an example for detailed operation explanations.

## PostgreSQL

### Installation and Configuration

PostgreSQL is a modern open-source object-relational database management system.

For individual users learning to use it, you can directly download the software installation package to set up a local environment. You can choose different versions according to different systems, and it also has a convenient graphical interface for starting, stopping, restarting services, and making related configurations. This article uses PostgreSQL 14 on macOS as an example. After installing and performing basic settings from the [official website](https://postgresapp.com), you can manage the local PostgreSQL service. The version may vary slightly, but the core functions are not much different.

#### Graphical Interface

Open the PostgreSQL.app application, and you will see the following interface:

![mac_postgres_interface](https://image.pseudoyu.com/images/mac_postgres_interface.png)

In this management interface, you can conveniently start and stop the PostgreSQL service. Clicking on the corresponding database also allows you to enter the command-line operation interface.

#### Command-line Interface

First, we add the `psql` path to the environment variables for subsequent use. I use `zsh`, so I add the following content to the `~/.zshrc` file:

```bash
# postgres
export PATH=${PATH}:/Applications/Postgres.app/Contents/Versions/14/bin
```

After that, enter `psql` in the terminal to access the PostgreSQL command-line interface. You can use the following command to view the psql command list:

```bash
psql --help
```

### Connecting to PostgreSQL

We can connect to the database using the following command:

```bash
# Connect to the database
psql -h <host> -p <port> -U <username> <database-name>
```

Of course, we can also use some third-party tools to connect to the database more conveniently. I currently use [TablePlus](http://tableplus.com), which supports PostgreSQL databases, and I recommend it.

### Command-line Interaction

PostgreSQL provides powerful command-line interaction functionality. We can use `\` + keyword to perform operations. We can view command details and help information by consulting the documentation or using the `\?` and `help` commands. Other commonly used commands are as follows:

```bash
# View help
help

# View psql command details
\?

# View databases (all)
\l

# View databases (specific)
\l <database-name>

# Connect to a database
\c <database-name>

# View methods
\df

# View tables (all)
\d

# View tables (tables only)
\dt

# View tables (specific)
\d <table-name>

# Execute SQL commands
\i <filepath>/<filename>

# Open expanded view
\x

# Export to CSV
\copy (SELECT * FROM person LEFT JOIN car ON person.car_id = car.id) TO 'path/to/output.csv' DELIMITER ',' CSV HEADER;

# Exit
\q
```

### Core Syntax

After configuring and connecting to the local PostgreSQL, we can perform some operations on the database. SQL language is mainly divided into the following four categories:

- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DQL (Data Query Language)
- DCL (Data Control Language)

#### DDL Operations

```sql
--- Create database
CREATE DATABASE <database-name>;

--- Delete database
DROP DATABASE <database-name>;
```

```bash
# Enter a specific database
\c <database-name>;
```

```sql
--- Create table (add constraints)
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50),
    email VARCHAR(150)
);

--- Modify table
ALTER TABLE person ADD PRIMARY KEY(id);

--- Delete column
ALTER TABLE person DROP column email;

--- Delete entire table
DROP TABLE person;
```

#### DML Operations

```sql
--- Insert data
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06');

--- Modify data content
UPDATE person SET email = 'ommar@gmail.com' WHERE id = 20;

--- Delete data content
DELETE FROM person WHERE id = 1;
```

You can use the `ON CONFLICT` keyword to handle conflicts:

```sql
--- Do nothing when a conflict occurs
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06') ON CONFLICT (id) DO NOTHING;

--- Update specified fields when a conflict occurs
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;
```

#### DQL Operations

You can query the table using the `SELECT` command. The most commonly used command to view the entire table is:

```sql
--- View all data in the table
SELECT * FROM person;

--- Query data (specific fields)
SELECT first_name, last_name FROM person;
```

You can use the `WHERE` keyword for conditional queries and combination queries with multiple conditions:

```sql
--- Query data (condition filtering, WHERE | AND | OR | comparison > | >= | < | <= | = | <>)
SELECT * FROM person WHERE gender = 'MALE' AND (country_of_birth = 'Poland' OR country_of_birth = 'China');
```

`IN`, `BETWEEN`, `LIKE`, and `ILIKE` are also some keywords that can be used flexibly for queries.

`IN` can help us filter multiple values of a certain field.

```sql
--- Query data (using IN keyword)
SELECT * FROM person WHERE country_of_birth IN ('China', 'Brazil', 'France');
```

`BETWEEN` can help us filter a range of a certain field.

```sql
--- Query data (using BETWEEN keyword)
SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2021-10-10' AND '2022-08-31';
```

`LIKE` can help us perform some fuzzy searches for inclusion relationships. `%` can match any character, `_` can match a single character. `ILIKE` is case-insensitive `LIKE`.

```sql
--- Query data (using LIKE/ILIKE keywords, _ | %)
SELECT * FROM person WHERE email LIKE '%@bloomberg.%';
SELECT * FROM person WHERE email LIKE '________@google.%';
SELECT * FROM person WHERE country_of_birth ILIKE 'p%';
```

In practical applications, the data volume of data tables is often very large, and data needs to be grouped according to corresponding conditions. This requires the use of the `GROUP BY` keyword, and `HAVING` is used for further filtering conditions. `GROUP BY` needs to be used in conjunction with aggregate functions.

```sql
--- Query data (using GROUP BY keyword for grouped queries, using HAVING keyword to add conditions, using AS for result aliases)
SELECT country_of_birth, COUNT(*) AS Amount FROM person GROUP BY country_of_birth HAVING Amount > 5 ORDER BY country_of_birth;
```

Sometimes we only need to return unique values and need to remove duplicate data. In this case, we can use the `DISTINCT` keyword.

```sql
--- Query data (remove duplicates)
SELECT DISTINCT country_of_birth FROM person;
```

In practical applications, it is also very likely that we need to rank certain product transaction volumes, arrange some values, or display blog posts in chronological order, etc. This requires the use of the `ORDER BY` keyword, which defaults to `ASC` ascending order, and can be manually set to `DESC` for descending order.

```sql
--- Query data (sort ASC | DESC)
SELECT * FROM person ORDER BY id, country_of_birth;
```

At the same time, some databases have very large amounts of data, and returning all data at once is resource-consuming. Therefore, we can use the `LIMIT` keyword to constrain the number of returned records, and use `OFFSET` to specify the offset.

```sql
--- Query data (specify quantity and offset)
SELECT * FROM person OFFSET 5 LIMIT 10;
SELECT * FROM person OFFSET 5 FETCH FIRST 5 ROW ONLY;
```

### Core Concepts

#### PRIMARY KEY

The primary key is the unique identity record in the data table, created and modified with the following commands:

```sql
--- Add primary key
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY
);

--- Modify primary key
ALTER TABLE person ADD PRIMARY KEY(id);
```

The primary key usually uses `SERIAL/BIGSERIAL` incremental `INT` values, or `UUID` can be used as the primary key.

```sql
CREATE TABLE person (
    id UUID NOT NULL PRIMARY KEY
);
```

#### FOREIGN KEY

A foreign key is a special type of primary key that is the primary key of another table, created and modified with the following commands:

```sql
--- Add foreign key
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    car_id BIGINT REFERENCES car (id),
    UNIQUE(car_id)
);

--- Modify foreign key
CREATE TABLE car (
    id BIGSERIAL NOT NULL PRIMARY KEY
)
```

#### JOIN

A join query refers to connecting data from multiple tables during a query to retrieve more information. In SQL, we can use the `JOIN` keyword to implement join queries, use the `LEFT JOIN` keyword to implement left join queries, and use the `RIGHT JOIN` keyword to implement right join queries.

```sql
--- JOIN query
SELECT * FROM person
JOIN car ON person.car_id = car.id

--- LEFT JOIN query
SELECT * FROM person
LEFT JOIN car ON person.car_id = car.id
```

You can use the `USING` keyword to simplify the use of the `ON` keyword.

```sql
SELECT * FROM person
LEFT JOIN car USING (car_id);
```

#### Constraints

CONSTRAINT is used to restrict the data in the data table. We can add constraints using the following command:

```sql
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender = 'Female' OR gender = 'Male');
```

For example, add `UNIQUE` to indicate uniqueness:

```sql
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(150) UNIQUE
);

ALTER TABLE person ADD CONTRAINT unique_email_address UNIQUE (email);
```

### Useful Techniques

#### Aggregate Functions

Many aggregate functions are built-in, such as `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, etc., used for aggregate calculations on data.

#### COALESCE

When querying data, we can use `COALESCE` to fill in default values:

```sql
--- Use COALESCE to fill in default values
SELECT COALESCE(email, 'Email Not Provided') FROM person;
```

#### NULLIF

Using the `NULLIF` keyword, when the second parameter is the same as the first, it returns `NULL`, otherwise it returns the first parameter. This is used to prevent errors such as division by zero.

```sql
SELECT COALESCE(10 / NULLIF(0, 0), 0);
```

#### Time

The display format for time is as follows:

```sql
SELECT NOW();
SELECT NOW()::DATE;
SELECT NOW()::TIME;
```

We can perform calculations on time:

```sql
SELECT NOW() - INTERVAL '1 YEAR';
SELECT NOW() + INTERVAL '10 MONTHS';
SELECT (NOW() - INTERVAL '3 DAYS')::DATE;
```

We can use `EXTRACT` to get a certain part of the time:

```sql
SELECT EXTRACT(YEAR FROM NOW());
SELECT EXTRACT(MONTH FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT EXTRACT(DOW FROM NOW());
SELECT EXTRACT(CENTURY FROM NOW());
```

We can use the `AGE` keyword to calculate age differences:

```sql
SELECT first_name, last_name, AGE(NOW(), date_of_birth) AS age FROM person;
```

### Extended Support

PostgreSQL provides many extensions to implement richer functionality.

#### Installing Extensions

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

#### View Extension Methods

```bash
df
```

#### Using Extension Methods

```sql
SELECT uuid_generate_v4();
```

## Conclusion

The above is my explanation of the basic knowledge and practical operations of PostgreSQL. I hope it's helpful to you.

## References

> 1. [PostgreSQL Official Website](http://www.postgresql.org)
> 2. [Postgres.app Official Website](https://postgresapp.com)
> 3. [TablePlus Official Website](https://tableplus.com)