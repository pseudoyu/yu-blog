---
title: "MySQL 基础知识与相关操作"
date: 2021-03-29T00:12:17+08:00
draft: false
tags: ["database", "mysql", "programming"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

数据库不论在基础知识学习还是真实企业业务场景中都很常用，也有很多调侃说日常工作总是离不开 CRUD，熟练主流关系型与数据库的使用是一个开发者基本的操作。本文将在 MacOS 系统下对 MySQL 这个流行的关系性数据库的基础知识与相关操作进行整理，以便于查阅。

## 数据与数据库概述

### 数据

首先，数据其实本质上是一种事实或者观察到的结果，是对客观事务的逻辑上的归纳总结，是信息的一种表现形式和载体。人们从很早的时候就开始管理数据（即使还没有这个概念），最初是由人工管理，而后来渐渐有了文件系统（就像图书馆一样，分门别类地管理不同信息），而随着计算机技术的发展，最后形成了用数据库进行管理的这种较为便捷高效的模式。

### 数据库

数据库是按照一定的数据结构来组织、存储和管理数据的一个仓库，主要特征为

- 结构化
- 可共享
- 冗余度小
- 独立性高
- 易于拓展

很好理解的是，按照不同关系/结构组织起来的数据具备不同的特征，同时也适用于不同的应用场景，目前主要分为层次数据库、网状数据库和关系数据库三种，而我们要着重介绍的 MySQL 就数据关系数据库。

### 数据库管理系统(DBMS)

数据库管理系统(DBMS)是对数据库进行各种操作的一个系统，一具有建立和维护数据库、对数据的存储进行组织管理、对数据库进行控制、定义数据、操纵数据以及管理数据之间的通信等核心功能，不同的数据库管理系统对数据库和数据的处理方式不同，数据呈现方式也不同，也往往需要根据数据规模、业务需求等场景选择合适的数据库管理系统，如在海量数据和高并发数据读写的情况下，关系性数据库的性能会下降得很厉害。

## 关系性数据库(RDBMS)

### 主要特征

关系性数据库主要以数据表的形式呈现，每一行为一条记录，每一列则为记录名称所对应的数据域(Field)。许多行列组成一张单表，而若干单表则组成数据库。用户/系统通过 SQL(结构化查询语言对数据库进行查询。

有些关系型数据库的操作具有事务性，即 ACID 规则

- 原子性(Atomicity)
- 一致性(Consistency)
- 隔离性(Isolation)
- 持久性(Durability)

原子性是指一系列事务操作要么都完成，要么都失败，不存在完成了一部分这样的情况，例如银行转账这样的场景里，转账行为发生后，发送方余额减少，而如果数据库出现了操作错误，接收方余额未增加，则会造成严重的问题。

一致性是指在事务执行完成后，整个数据库的数据是一致的，不应存在数据库内同一数据不同步的情况。

隔离性则是指不同的事务之间应该独立进行运行、互不干扰的，当然，这样会牺牲一定的效率，但对数据的准确性等提供了较好保障。

持久性则是指当一个事务执行完成后，它对数据库进行的更改、对系统产生的影响是永久的。

### 数据完整性

数据完整性是数据库很重要的一个要求和属性，是指存储在数据库中的数据应该保持一致性和可靠性，主要分为以下四种

- 实体完整性
- 域完整性
- 参照完整性
- 用户定义完整性

实体完整性要求每张数据表都有一个唯一的标识符，每张表中的主键字段不能为空且不能重复，这主要是指表中的数据都可以被唯一区分。

域完整性则是通过对表中列做一些额外限制，如限制数据类型、检查约束、设置默认值、是否允许空值以及值域范围等。

```sql
--- 在创建表时对字段进行唯一性的约束
create table person (
    id int not null auto_increment primary key,
    name varchar(30),
    id_number varchar(18) unique
);
```

参照完整性是指数据库不允许引用不存在的实体，数据库的表与其他表之间往往存在一些关联，可以通过外键约束来保障其完整性。

而用户自定义完整性则是根据具体应用场景和涉及到数据来对数据进行一些语义方面的限制，如余额不能为负数等，一般用设定规则、存储过程和触发器等来进行约束和限制。

### 主流 RDBMS

目前主流的关系型数据库有以下几种

- SQL Server
- Sybase
- DB2
- Oracle
- MySQL

企业和个人用得比较多的是 Oracle 和 MySQL 两种，接下来也会以 MySQL 为例进行详细的操作讲解。

## MySQL

### 安装与启动

MySQL 是由 Sun 公司（后被 Oracle 公司收购）开发维护的一种很流行的小型数据库系统，由于体积很小且运行数据快，被很多中小型企业/网站采用，也具备较完整的开发和维护生态。

作为个人用户学习使用，可以下载社区版（开源）进行使用本地搭建环境，可以根据不同的系统选择不同的版本，也具备较便捷的图形界面供大家进行服务的开启、关闭、重启以及进行相关的配置等。本文以 MacOS 系统下的`MySQL 8.0.21`为例，在安装及进行基本设置后，就可以对本机 MySQL 服务进行管理，版本可能会略有差别，但核心功能差别不大。

#### 图形界面

打开系统偏好设置，可以看到如下界面

![mac_mysql_manage](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mac_mysql_manage.png)

点击 MySQL 图标即可进入详细管理界面

![mac_mysql_service](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mac_mysql_service.png)

在这个管理界面可以很方便地进行 MySQL 服务的开启与关闭，也可以将其设置为开机自启等操作，`Configuration`中也可以进行进一步的设置，但更建议在命令行进行。

#### 命令行界面

当然，也可以在命令行中进行启动

```sh
//启动MySQL
sudo /usr/local/mysql/support-files/mysql.server start

//关闭MySQL
sudo /usr/local/mysql/support-files/mysql.server stop
```

效果如下

![mac_mysql_cli](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mac_mysql_cli.png)

当然也可以通过设置一些 alias 来简化命令，但是既然有比较方便的管理界面了，也就不折腾了，如果在一些没有图形界面的 linux 环境下进行操作，则需要命令行操作。

### 连接 MySQL

安装和启动完成后 即可通过命令行连接 MySQL 并进行一些基本操作了

```sh
mysql -h localhost -u root -p

//输入安装时设置的密码

//查看状态
status;
```

![mysql_connect](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_connect.png)

而除了通过命令行连接外，MacOS 平台上也有一个很好用的客户端`Sequel Pro`，提供了大多数需要的功能，而由于正式版存在崩溃问题且已经不再维护，建议下载测试版 [Sequel Pro 测试版](https://sequelpro.com/test-builds)，可以很方便地连接至本地/远程服务器 MySQL 服务

![sequel_pro_connect](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sequel_pro_connect.png)

并查询数据库的结构、内容及执行 SQL 命令

![sequel_pro_manage](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sequel_pro_manage.png)

这是目前我使用下来非常强大且轻量级的一个客户端，建议大家使用！

### SQL 命令

经过了本地 MySQL 配置与连接后，我们就可以对数据库进行一些操作了，SQL 语言主要分为以下四类

- DDL 数据定义语言（Data Definition Language）
- DML 数据操纵语言（Data Manipulation Language）
- DQL 数据查询语言（Data Query Language）
- DCL 数据控制语言（Data Control Language）

接下来我们将通过实战完成一系列操作

#### DDL 操作

```sql
--- 创建数据库
create database learn_test;

--- 显示所有数据库
show databases;

--- 删除数据库
drop database mydb;
```

![mysql_ddl](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_ddl.png)

```sql
--- 进入某个数据库
use learn_test;

--- 创建一个简单的数据表
create table contacts (
    id int not null auto_increment primary key,
    name varchar(30),
    phone varchar(20)
);

--- 添加字段
alter table contacts add sex varchar(1);

--- 修改字段
alter table contacts modify sex tinyint;

--- 删除字段
alter table contacts drop column sex;

--- 删除全表
drop table contacts;
```

为了方便演示，这些操作都将在`Sequel Pro`客户端中进行，操作后我们的表结构如下

![mysql_learn_test_ddl](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_learn_test_ddl.png)

#### DML 操作

```sql
--- 插入多条数据
insert into contacts (name, phone, sex) values('张三', '13100000000', 1), ('李四', '13100000001', 1), ('王五', '13100000002', 2);

--- 修改数据内容
update contacts set sex = 1 where name = '王五';

--- 删除数据内容
delete * from contacts where id = 3;
```

#### DQL 操作

MySQL 可以通过`select`命令来对表进行查询，最常用的查看全表命令为

```sql
--- 查看表的全部数据
select * from contacts;
```

还可以通过`where`关键字来进行条件查询、以及多个条件的组合查询

```sql
--- 组合条件进行查询
select * from contacts where id = 1 or name = "李四";
```

![mysql_contacts_dql](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql.png)

`IN`和`LIKE`也是两个可以很灵活用于查询的关键字。

`IN`可以帮助我们过滤某个字段的多个值

```sql
--- 查询id在(1,3)中的数据
select * from contacts where id in(1,3);
```

![mysql_contacts_dql_in](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql_in.png)

同时，`IN`和`EXISTS`也可以用于子查询

```sql
--- 子查询 IN
select A.*
from student A
where A.stu_no in(
        select B.stu_no from score B
);

--- 子查询 EXISTS
select A.*
from student A
where exists(
        select * from score B
        where A.stu_no = B.stu.no
);
```

`LIKE`可以帮助我们进行一些包含关系的模糊搜索，`%`可以匹配任一个字符，`_`可以匹配单个字符

```sql
--- 查询所有姓张的联系人
select * from contacts where name like '张%';
```

![mysql_contacts_dql_like_2](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql_like_2.png)

```sql
--- 查询所有名字以四结尾且为两个字的的联系人
select * from contacts where name like '_四';
```

![mysql_contacts_dql_like](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql_like.png)


实际应用中，往往数据表的数据量非常庞大，会对数据根据相应条件进行分组，这就要用到`GROUP BY`关键字，以及`HAVING`用于进一步筛选条件。`GROUP BY`需要配合聚合函数进行使用。

```sql
--- 统计男联系人数量
select case sex
            when 1 then "男" 
            when 2 then "女" 
            else "未知" end as 性别,
        count(*) as 人数
from contacts 
group by sex
having sex = 1;
```

![mysql_contacts_dql_group_by](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql_group_by.png)

而也可以通过`GROUP_CONCAT`来结合一些具体的数据

```sql
--- 按性别显示不同性别联系人的列表及总数
select case sex
            when 1 then "男" 
            when 2 then "女" 
            else "未知" end as 性别,
        group_concat(name order by name desc separator ' | '),
        count(*) as 人数
from contacts 
group by sex;
```

![mysql_contacts_dql_group_concat](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_dql_group_concat.png)

有时候我们只需要返回唯一值，而需要去掉重复数据，则可以使用`DISTINCT`关键字

```sql
--- 在查询时对字段进行去重
select distinc sex from contacts;
```

在实际应用中，还很有可能会需要对某些商品交易量进行排名、对一些数值进行排列或博客文章中按照时间线后进行顺序显示等，这就需要用到`ORDER BY`这一关键字，它默认为`ASC`升序排列，可以通过手动设置`DESC`来实现降序。

同时，有的数据库数据量非常大，一次返回所有的数据比较消耗资源，因此也可以使用`LIMIT`关键字来约束返回的记录数，同时，也可以实现分页。

```sql
select * from contacts order by id desc limit 5;
```

![mysql_dql_order_by_limit](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_dql_order_by_limit.png)

### 内置函数

MySQL 也有很多常见的内置函数，可以帮助用户更方便处理各种数据，简化操作，大多数功能都很直观，不作一一说明了

![mysql_functions](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_functions.png)

其中值得注意的是，聚合函数是对一组值进行计算并返回单个值。

### 流程控制

MySQL 有一种类似于编程语言中的 if else 或 switch 的流程控制语句，以实现复杂的应用逻辑

```sql
--- 选取数据并且把性别以中文标识
select name, phone, case sex
                        when 1 then "男"
                        when 2 then "女"
                        else "未知" end
                    as sex
from contacts;
```

![mysql_contacts_flow_control](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_contacts_flow_control.png)

### 表的连接

不同的表可以通过一定连接条件发生关联，主要有自连接、内连接和外连接三种，其中外连接又分为左外连接、右外连接和全外连接三种，他们的区别如下

![mysql_table_join](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mysql_table_join.png)

而自连接是一种特殊的连接方式，通过在逻辑上生成多张表以实现复杂的层次结构，常应用于区域表、菜单表和商品分类表等，语法如下

```sql
--- 自连接语法
select A.cloumn, B.column
from table A, table B
where A.column = B.column;
```

## 总结

学完了关系型数据库，那非关系型数据库又是怎样的呢？后续将会对 Redis 这一使用广泛的非关系性数据库进行整理，敬请期待！

## 参考资料

> 1. [MySQL 官网](https://www.mysql.com)
> 2. [Sequel Pro 官网](https://sequelpro.com)