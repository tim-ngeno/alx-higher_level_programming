# 0x0D. SQL - Introduction

This file provides detailed explanations and code examples for various database-related terms and operations using MySQL. 

## Table of Contents

- [What's a Database](#whats-a-database)
- [What's a Relational Database](#whats-a-relational-database)
- [What Does SQL Stand For](#what-does-sql-stand-for)
- [What's MySQL](#whats-mysql)
- [How to Create a Database in MySQL](#how-to-create-a-database-in-mysql)
- [DDL and DML](#ddl-and-dml)
- [CREATE and ALTER a Table](#create-and-alter-a-table)
- [SELECT Data from a Table](#select-data-from-a-table)
- [INSERT, UPDATE, and DELETE Data](#insert-update-and-delete-data)
- [Subqueries](#subqueries)
- [Using MySQL Functions](#using-mysql-functions)

## What's a Database

A database is a structured collection of data that is organized and stored for efficient retrieval and manipulation.

It can store various types of information, such as text, numbers, dates, and more.

```sql
-- Example: Creating a Database
CREATE DATABASE mydatabase;
```

## What's a Relational Database

A relational database is a type of database that organizes data into structured tables with predefined relationships between them. It uses SQL to manage and query the data.

## What Does SQL Stand For

SQL stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases.

## What's MySQL

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It provides a platform for creating, managing, and querying databases.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE dbname;
```

## DDL and DML

DDL stands for Data Definition Language, which includes commands for defining and managing database structures (e.g., CREATE, ALTER).

DML stands for Data Manipulation Language, which includes commands for interacting with data (e.g., SELECT, INSERT, UPDATE, DELETE).

## CREATE and ALTER a Table

You can create a new table using the `CREATE TABLE` command:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```

To alter an existing table, you can use the `ALTER TABLE` command:

```sql
ALTER TABLE students ADD COLUMN email VARCHAR(100);
```

## SELECT Data from a Table

Retrieve data from a table using the `SELECT` statement:

```sql
SELECT name, age FROM students WHERE age > 20;
```

## INSERT, UPDATE, and DELETE Data

Insert new data using `INSERT INTO`:

```sql
INSERT INTO students (name, age) VALUES ('John', 25);
```

Update existing data using `UPDATE`:

```sql
UPDATE students SET age = 26 WHERE name = 'John';
```

Delete data using `DELETE`:

```sql
DELETE FROM students WHERE age < 18;
```

## Subqueries

A subquery is a query nested within another query. It can be used to retrieve data for further processing or filtering.

```sql
SELECT name FROM students WHERE age IN (SELECT age FROM other_table);
```

## Using MySQL Functions

MySQL provides various built-in functions for tasks like calculations, string manipulation, and date formatting.

```sql
SELECT AVG(age) AS average_age FROM students;
```

You can leverage MySQL functions to perform a wide range of operations on your data.

```sql
-- Calculate the total number of students
SELECT COUNT(*) AS total_students FROM students;

-- Concatenate first and last names
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

-- Format dates using DATE_FORMAT
SELECT event_name, DATE_FORMAT(event_date, '%Y-%m-%d') AS formatted_date FROM events;
```

## Displaying Output

When querying data, you can format the output to meet your needs.

```sql
-- Display distinct age values
SELECT DISTINCT age FROM customers;

-- Order results in descending order
SELECT product_name, unit_price FROM products ORDER BY unit_price DESC;

-- Limit the number of results
SELECT category_name FROM categories LIMIT 5;
```

## Joining Tables

Tables can be combined using joins to retrieve related data.

```sql
-- Inner join to retrieve orders with customer information
SELECT orders.order_id, customers.customer_name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;

-- Left join to get all products with or without orders
SELECT products.product_name, order_details.order_id
FROM products
LEFT JOIN order_details ON products.product_id = order_details.product_id;
```

## Aggregating Data

Aggregate functions allow you to summarize data.

```sql
-- Calculate the total revenue
SELECT SUM(order_total) AS total_revenue FROM orders;

-- Find the highest unit price
SELECT MAX(unit_price) AS highest_price FROM products;

-- Calculate average employee age
SELECT AVG(age) AS average_age FROM employees;
```

## Conclusion

This is an overview of key database concepts and SQL operations using MySQL. From creating databases, defining tables, querying data, performing CRUD operations, utilizing functions, and more.

[MySQL documentation](https://dev.mysql.com/doc/)
