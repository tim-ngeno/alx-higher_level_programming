# Object Relational Mappers (ORM)

Object Relational Mappers, often abbreviated as ORM, is a programming technique that allows developers to interact with their database, like they would with SQL. In other words, the ORM allows you to work with objects in your programming language (like Python) to interact with a database without writing raw SQL queries. Instead, the ORM would handle all SQL operations behind the scenes, including CRUD (Create, Read, Update, Delete) operations.

Object-Relational Mapping, especially with tools like SQLAlchemy, bridges the gap between object-oriented programming and relational databases. It allows for more maintainable, secure, and readable code, eliminating the need for manual SQL writing for most operations.


## Advantages of ORM:
- **Abstraction:** ORM provides a high-level abstraction upon a relational database that allows developers to write Python code instead of SQL to create, read, update and delete data and schemas in their database.

- **Database Agnostic:** ORM tools usually provide a database-agnostic query API, which allows the same code to work on multiple database systems.

- **Maintainability:** Writing raw SQL in code can get very messy, especially for complex queries. With ORM, the code is cleaner and more maintainable.

## SQLAlchemy: A Popular ORM for Python

[SQLAlchemy](https://www.sqlalchemy.org/) is a popular ORM for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access. With SQLAlchemy, you can work with relational databases in a more Pythonic way!


## Why ORM and Why SQLAlchemy?

Traditional database access using SQL can be quite tedious and error-prone, especially for large applications. Every database operation would require the developer to write and maintain raw SQL statements, handle connections, manage transactions, and take care of data serialization and deserialization.

ORMs, like SQLAlchemy, offer a solution to these problems. They allow developers to interact with databases using high-level objects without the need to write raw SQL. This makes development faster, reduces the risk of SQL injection attacks, and offers more maintainability.





### How to connect to a MySQL database from a Python script using SQLAlchemy:

```python
from sqlalchemy import create_engine

# The format of the connection string is:
# dialect+driver://username:password@host:port/database
DATABASE_URL = "mysql+mysqlclient://username:password@localhost/mydatabase"
engine = create_engine(DATABASE_URL)
```

### How to SELECT rows in a MySQL table from a Python script:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Assume we have a `User` model
for user in session.query(User).filter_by(name='John'):
    print(user.id, user.name)
```

### How to INSERT rows in a MySQL table from a Python script:

```python
new_user = User(name="John", age=28)
session.add(new_user)
session.commit()
```

### How to map a Python Class to a MySQL table:

With SQLAlchemy, you can define a class as a representation of a table in your database:

```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
```




### Updating and Deleting Rows with SQLAlchemy:

To update rows in the database, you can modify the object attributes and then commit the changes. For deleting rows, you can use the `delete()` method.

**Updating Rows:**

```python
# Fetch the object you want to update
user = session.query(User).filter_by(name='John').first()
user.age = 29

# Commit the changes
session.commit()
```

**Deleting Rows:**

```python
# Fetch the object you want to delete
user = session.query(User).filter_by(name='John').first()

# Delete the object
session.delete(user)

# Commit the changes
session.commit()
```

### Relationships in SQLAlchemy:

One of the strengths of SQLAlchemy is its ability to define relationships between tables (like one-to-many, many-to-many). This allows you to model your database tables in a way that closely matches the real-world scenarios.

For instance, consider two tables: `User` and `Post`. A user can have many posts, so there's a one-to-many relationship between these tables.

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    title = Column(String(100))
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))

    # This creates a one-to-many relationship
    user = relationship("User", back_populates="posts")

User.posts = relationship("Post", order_by=Post.id, back_populates="user")
```




### How to create a Python Virtual Environment:

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python environments for them.

```bash
# Install virtualenv
pip install virtualenv

# Create a virtual environment
virtualenv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate

# On MacOS/Linux:
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

In the virtual environment, you can install the required packages without affecting the global Python installation. For SQLAlchemy work, you might want to install packages like `sqlalchemy` and `mysqlclient` within the virtual environment.
