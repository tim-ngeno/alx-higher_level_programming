# 0x0E. SQL - More queries

## Table of Contents:

- [How to Create a New MySQL User](#how-to-create-a-new-mysql-user)
- [How to Manage Privileges for a User to a Database or Table](#how-to-manage-privileges-for-a-user-to-a-database-or-table)
- [What's a PRIMARY KEY](#whats-a-primary-key)
- [What's a FOREIGN KEY](#whats-a-foreign-key)
- [How to Use NOT NULL and UNIQUE Constraints](#how-to-use-not-null-and-unique-constraints)
- [How to Retrieve Data from Multiple Tables in One Request](#how-to-retrieve-data-from-multiple-tables-in-one-request)
- [What Are Subqueries](#what-are-subqueries)
- [What Are JOIN and UNION](#what-are-join-and-union)

## How to Create a New MySQL User

To create a new MySQL user, you can use the `CREATE USER` statement followed by the `IDENTIFIED BY` clause to set a password. For example:

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

## How to Manage Privileges for a User to a Database or Table

To manage privileges for a user, you can use the `GRANT` statement to assign specific privileges to a user on a database or table. For example:

```sql
GRANT SELECT, INSERT, UPDATE ON database.table TO 'username'@'localhost';
```

## What's a PRIMARY KEY

A PRIMARY KEY is a column or a combination of columns that uniquely identify each row in a table. It ensures data integrity and provides a quick way to retrieve specific records.

## What's a FOREIGN KEY

A FOREIGN KEY is a column that establishes a link between two tables. It enforces referential integrity by ensuring values in one table match values in another table.

## How to Use NOT NULL and UNIQUE Constraints

The `NOT NULL` constraint ensures that a column cannot have a NULL value. The `UNIQUE` constraint ensures that all values in a column are unique.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    email VARCHAR(256) UNIQUE
);
```

## How to Retrieve Data from Multiple Tables in One Request

You can retrieve data from multiple tables using the `JOIN` statement. It combines rows from different tables based on related columns.

```sql
SELECT customers.name, orders.order_date
FROM customers
JOIN orders ON customers.id = orders.customer_id;
```

## What Are Subqueries

A subquery is a query embedded within another query. It can be used to retrieve data that will be used in the main query.

```sql
SELECT name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

## What Are JOIN and UNION

`JOIN` combines rows from different tables based on related columns. `UNION` combines the results of two or more `SELECT` statements into a single result set.

```sql
SELECT name FROM customers WHERE country = 'USA'
UNION
SELECT name FROM customers WHERE country = 'Canada';
```


---