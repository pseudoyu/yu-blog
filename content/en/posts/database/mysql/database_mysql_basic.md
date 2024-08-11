---
title: "MySQL Fundamentals and Practice"
date: 2021-03-29T00:12:17+08:00
draft: false
tags: ["database", "mysql", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Databases are commonly used in both foundational learning and real enterprise business scenarios. There's often a jest that daily work always revolves around CRUD operations. Proficiency in using mainstream relational databases is a fundamental skill for developers. This article will provide an overview of the basic knowledge and related operations of MySQL, a popular relational database, on the MacOS system for easy reference.

## Overview of Data and Databases

### Data

Fundamentally, data is a type of fact or observed result, a logical summary of objective matters, and a form and carrier of information. People have been managing data since ancient times (even before the concept existed), initially through manual management, later through file systems (like libraries, managing different information by categories), and finally, with the development of computer technology, forming the more convenient and efficient mode of database management.

### Database

A database is a repository that organizes, stores, and manages data according to a certain data structure. Its main characteristics are:

- Structured
- Sharable
- Low redundancy
- High independence
- Easy to expand

It's easy to understand that data organized according to different relationships/structures have different characteristics and are suitable for different application scenarios. Currently, there are mainly three types: hierarchical databases, network databases, and relational databases. MySQL, which we will focus on, is a relational database.

### Database Management System (DBMS)

A Database Management System (DBMS) is a system that performs various operations on databases. It has core functions such as establishing and maintaining databases, organizing and managing data storage, controlling databases, defining data, manipulating data, and managing communication between data. Different database management systems handle databases and data differently, and the data presentation methods also vary. The choice of database management system often needs to be based on data scale, business requirements, and other scenarios. For instance, in cases of massive data and high-concurrency data read and write operations, the performance of relational databases can deteriorate significantly.

## Relational Database Management System (RDBMS)

### Main Features

Relational databases primarily present data in the form of tables, with each row being a record and each column being the data field corresponding to the record name. Many rows and columns form a single table, and several single tables form a database. Users/systems query the database through SQL (Structured Query Language).

Some relational database operations have transactional properties, namely the ACID rules:

- Atomicity
- Consistency
- Isolation
- Durability

Atomicity means that a series of transaction operations either all complete or all fail; there is no situation where only part is completed. For example, in a bank transfer scenario, after the transfer occurs, the sender's balance decreases, and if a database operation error occurs and the receiver's balance doesn't increase, it would cause serious problems.

Consistency means that after a transaction is completed, the data in the entire database is consistent, and there should not be situations where the same data is out of sync within the database.

Isolation means that different transactions should run independently and without interference. Of course, this sacrifices some efficiency but provides better guarantees for data accuracy.

Durability means that when a transaction is completed, its changes to the database and its effects on the system are permanent.

### Data Integrity

Data integrity is a crucial requirement and attribute of databases, referring to the consistency and reliability of data stored in the database. It is mainly divided into four types:

- Entity integrity
- Domain integrity
- Referential integrity
- User-defined integrity

Entity integrity requires each data table to have a unique identifier, and the primary key field in each table cannot be null or duplicate, mainly meaning that all data in the table can be uniquely distinguished.

Domain integrity is to make some additional restrictions on the columns in the table, such as restricting data types, check constraints, setting default values, whether to allow null values, and value range, etc.

```sql
--- Constraining field uniqueness when creating a table
create table person (
    id int not null auto_increment primary key,
    name varchar(30),
    id_number varchar(18) unique
);
```

Referential integrity means that the database does not allow referencing non-existent entities. Tables in the database often have some associations with other tables, and referential integrity can be ensured through foreign key constraints.

User-defined integrity is to place some semantic restrictions on data according to specific application scenarios and data involved, such as balance cannot be negative, etc. It is generally constrained and restricted by setting rules, stored procedures, and triggers.

### Mainstream RDBMS

Currently, the mainstream relational database management systems include:

- SQL Server
- Sybase
- DB2
- Oracle
- MySQL

Oracle and MySQL are the two most commonly used by enterprises and individuals. The following will provide a detailed operational explanation using MySQL as an example.

## MySQL

### Installation and Startup

MySQL is a popular small database system developed and maintained by Sun Microsystems (later acquired by Oracle Corporation). Due to its small size and fast data operation, it is adopted by many small and medium-sized enterprises/websites and has a relatively complete development and maintenance ecosystem.

For individual users learning to use it, you can download the community version (open source) to set up a local environment. You can choose different versions according to different systems, and there is also a convenient graphical interface for starting, stopping, restarting the service, and making related configurations. This article takes `MySQL 8.0.21` on the MacOS system as an example. After installation and basic setup, you can manage the local MySQL service. The version may be slightly different, but the core functionalities are not much different.

#### Graphical Interface

Open System Preferences, and you can see the following interface

![mac_mysql_manage](https://image.pseudoyu.com/images/mac_mysql_manage.png)

Click on the MySQL icon to enter the detailed management interface

![mac_mysql_service](https://image.pseudoyu.com/images/mac_mysql_service.png)

In this management interface, you can conveniently start and stop the MySQL service, and also set it to start automatically at boot, etc. You can also make further settings in `Configuration`, but it is more recommended to do so in the command line.

#### Command Line Interface

Of course, you can also start it in the command line

```sh
//Start MySQL
sudo /usr/local/mysql/support-files/mysql.server start

//Stop MySQL
sudo /usr/local/mysql/support-files/mysql.server stop
```

The effect is as follows

![mac_mysql_cli](https://image.pseudoyu.com/images/mac_mysql_cli.png)

Of course, you can also set some aliases to simplify commands, but since there is a convenient management interface, there's no need to bother. If you are operating in a Linux environment without a graphical interface, you will need to use command line operations.

### Connecting to MySQL

After installation and startup, you can connect to MySQL through the command line and perform some basic operations

```sh
mysql -h localhost -u root -p

//Enter the password set during installation

//View status
status;
```

![mysql_connect](https://image.pseudoyu.com/images/mysql_connect.png)

In addition to connecting through the command line, there is also a very useful client `Sequel Pro` on the MacOS platform, which provides most of the needed functions. Due to crash issues in the official version and it is no longer maintained, it is recommended to download the test version [Sequel Pro Test Version](https://sequelpro.com/test-builds), which can conveniently connect to local/remote server MySQL services

![sequel_pro_connect](https://image.pseudoyu.com/images/sequel_pro_connect.png)

And query the structure and content of the database and execute SQL commands

![sequel_pro_manage](https://image.pseudoyu.com/images/sequel_pro_manage.png)

This is a very powerful and lightweight client that I have used so far, and I recommend everyone to use it!

### SQL Commands

After local MySQL configuration and connection, we can perform some operations on the database. SQL language is mainly divided into the following four categories:

- DDL Data Definition Language
- DML Data Manipulation Language
- DQL Data Query Language
- DCL Data Control Language

Next, we will complete a series of operations through practice

#### DDL Operations

```sql
--- Create database
create database learn_test;

--- Show all databases
show databases;

--- Delete database
drop database mydb;
```

![mysql_ddl](https://image.pseudoyu.com/images/mysql_ddl.png)

```sql
--- Enter a certain database
use learn_test;

--- Create a simple data table
create table contacts (
    id int not null auto_increment primary key,
    name varchar(30),
    phone varchar(20)
);

--- Add field
alter table contacts add sex varchar(1);

--- Modify field
alter table contacts modify sex tinyint;

--- Delete field
alter table contacts drop column sex;

--- Delete entire table
drop table contacts;
```

For convenience of demonstration, these operations will be performed in the `Sequel Pro` client. After the operation, our table structure is as follows

![mysql_learn_test_ddl](https://image.pseudoyu.com/images/mysql_learn_test_ddl.png)

#### DML Operations

```sql
--- Insert multiple data
insert into contacts (name, phone, sex) values('Zhang San', '13100000000', 1), ('Li Si', '13100000001', 1), ('Wang Wu', '13100000002', 2);

--- Modify data content
update contacts set sex = 1 where name = 'Wang Wu';

--- Delete data content
delete * from contacts where id = 3;
```

#### DQL Operations

MySQL can query the table through the `select` command. The most commonly used command to view the entire table is

```sql
--- View all data in the table
select * from contacts;
```

You can also use the `where` keyword for conditional queries and combined queries with multiple conditions

```sql
--- Combined condition query
select * from contacts where id = 1 or name = "Li Si";
```

![mysql_contacts_dql](https://image.pseudoyu.com/images/mysql_contacts_dql.png)

`IN` and `LIKE` are also two keywords that can be used flexibly for queries.

`IN` can help us filter multiple values of a certain field

```sql
--- Query data with id in (1,3)
select * from contacts where id in(1,3);
```

![mysql_contacts_dql_in](https://image.pseudoyu.com/images/mysql_contacts_dql_in.png)

Also, `IN` and `EXISTS` can be used for subqueries

```sql
--- Subquery IN
select A.*
from student A
where A.stu_no in(
        select B.stu_no from score B
);

--- Subquery EXISTS
select A.*
from student A
where exists(
        select * from score B
        where A.stu_no = B.stu.no
);
```

`LIKE` can help us perform some fuzzy searches of containment relationships, `%` can match any character, `_` can match a single character

```sql
--- Query all contacts surnamed Zhang
select * from contacts where name like 'Zhang%';
```

![mysql_contacts_dql_like_2](https://image.pseudoyu.com/images/mysql_contacts_dql_like_2.png)

```sql
--- Query all contacts whose names end with 'Si' and have two characters
select * from contacts where name like '_Si';
```

![mysql_contacts_dql_like](https://image.pseudoyu.com/images/mysql_contacts_dql_like.png)

In practical applications, the data volume of data tables is often very large, and data needs to be grouped according to corresponding conditions. This requires the use of the `GROUP BY` keyword, and `HAVING` for further filtering conditions. `GROUP BY` needs to be used in conjunction with aggregate functions.

```sql
--- Count the number of male contacts
select case sex
            when 1 then "Male"
            when 2 then "Female"
            else "Unknown" end as Gender,
        count(*) as Count
from contacts
group by sex
having sex = 1;
```

![mysql_contacts_dql_group_by](https://image.pseudoyu.com/images/mysql_contacts_dql_group_by.png)

And you can also use `GROUP_CONCAT` to combine some specific data

```sql
--- Display the list and total number of contacts by gender
select case sex
            when 1 then "Male"
            when 2 then "Female"
            else "Unknown" end as Gender,
        group_concat(name order by name desc separator ' | '),
        count(*) as Count
from contacts
group by sex;
```

![mysql_contacts_dql_group_concat](https://image.pseudoyu.com/images/mysql_contacts_dql_group_concat.png)

Sometimes we only need to return unique values and need to remove duplicate data, then we can use the `DISTINCT` keyword

```sql
--- Remove duplicates when querying fields
select distinct sex from contacts;
```

In practical applications, it may also be necessary to rank certain product transaction volumes, arrange some values, or display blog posts in chronological order, etc. This requires the use of the `ORDER BY` keyword, which defaults to `ASC` ascending order and can be set to `DESC` manually to achieve descending order.

At the same time, some databases have a very large amount of data, and returning all the data at once is resource-consuming. Therefore, you can also use the `LIMIT` keyword to restrict the number of returned records, and at the same time, achieve pagination.

```sql
select * from contacts order by id desc limit 5;
```

![mysql_dql_order_by_limit](https://image.pseudoyu.com/images/mysql_dql_order_by_limit.png)

### Built-in Functions

MySQL also has many common built-in functions that can help users handle various data more conveniently and simplify operations. Most functions are intuitive and will not be explained one by one.

![mysql_functions](https://image.pseudoyu.com/images/mysql_functions.png)

It's worth noting that aggregate functions perform calculations on a group of values and return a single value.

### Flow Control

MySQL has a flow control statement similar to if-else or switch in programming languages to implement complex application logic

```sql
--- Select data and mark gender in Chinese
select name, phone, case sex
                        when 1 then "Male"
                        when 2 then "Female"
                        else "Unknown" end
                    as sex
from contacts;
```

![mysql_contacts_flow_control](https://image.pseudoyu.com/images/mysql_contacts_flow_control.png)

### Table Joins

Different tables can be associated through certain join conditions. There are mainly three types: self join, inner join, and outer join. Outer join is further divided into left outer join, right outer join, and full outer join. Their differences are as follows:

![mysql_table_join](https://image.pseudoyu.com/images/mysql_table_join.png)

Self join is a special join method that logically generates multiple tables to achieve complex hierarchical structures. It is commonly applied to area tables, menu tables, and product category tables, etc. The syntax is as follows:

```sql
--- Self join syntax
select A.column, B.column
from table A, table B
where A.column = B.column;
```

## Conclusion

Now that we've learned about relational databases, what about non-relational databases? In the future, we will organize information about Redis, a widely used non-relational database. Stay tuned!

## References

> 1. [MySQL Official Website](https://www.mysql.com)
> 2. [Sequel Pro Official Website](https://sequelpro.com)