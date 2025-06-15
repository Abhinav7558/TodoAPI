# FastAPI Todo Application

A robust Todo list application built with Python and FastAPI. This project demonstrates a complete backend solution including user authentication, database integration with SQLAlchemy, schema migrations with Alembic, and a full test suite using Pytest.

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0+-green.svg)](https://fastapi.tiangolo.com/)
[![Alembic](https://img.shields.io/badge/Alembic-1.16.0+-orange.svg)](https://alembic.sqlalchemy.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.0+-blueviolet.svg)](https://pytest.org/)

## Features

- **User Management**: User registration and login.
- **Authentication**: Secure token-based authentication using JWT.
- **Todo Management**: Full CRUD (Create, Read, Update, Delete) operations for todo items.
- **Authorization**: Todos are user-specific; users can only access their own todos.
- **Admin Panel**: A separate router for administrative actions.
- **Database Migrations**: Uses Alembic to manage database schema changes, making it easy to evolve the data model.
- **Testing**: Comprehensive unit and integration tests written with Pytest.
- **Interactive API Docs**: Automatic, interactive API documentation provided by FastAPI (via Swagger UI).

## Technology Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Database**: [SQLite](https://www.sqlite.org/index.html)
- **Testing**: [Pytest](https://docs.pytest.org/)
- **Password Hashing**: [bcrypt](https://pypi.org/project/bcrypt/)
- **Authentication**: [python-jose](https://pypi.org/project/python-jose/) for JWT tokens
- **Server**: [Uvicorn](https://www.uvicorn.org/)

## Project Structure

```
Todoapp/
│
├── alembic/ # Alembic migration scripts and environment
├── routers/ # API endpoint routers
│ ├── init.py
│ ├── admin.py
│ ├── auth.py
│ ├── todos.py
│ └── users.py
│
├── tests/ # Pytest test files
│ ├── init.py
│ ├── test_admin.py
│ ├── test_auth.py
│ ├── test_main.py
│ ├── test_todos.py
│ ├── test_users.py
│ └── utils.py # Test utilities and fixtures
│
├── alembic.ini # Alembic configuration
├── database.py # SQLAlchemy database setup and session management
├── main.py # Main FastAPI application entry point
├── models.py # SQLAlchemy ORM models
├── requirements.txt # Project dependencies (you should create this)
└── README.md

```

## Setup and Installation

Follow these steps to get the application running locally.

### 1. Clone the Repository

```bash
git clone
cd Todoapp
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

#### For macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages from requirements.txt.

```bash
pip install -r requirements.txt
```

### 4. Setup the Database

This project uses Alembic to manage the database schema. Run the following command to apply all migrations and create the todosapp.db file with the correct tables.

```bash
alembic upgrade head
```

### 5. Running the Application

To run the application in a local development environment, use uvicorn.

```bash
uvicorn main:app --reload
```

API documentation at:
Swagger UI: http://127.0.0.1:8000/docs

### 6. Running Tests

This project uses pytest for testing. The tests are configured to use a separate in-memory SQLite database testdb.db file to avoid interfering with development data.
To run the entire test suite, simply execute:

```bash
pytest
```

For more verbose output, you can use:

```bash
pytest -v
```

### 7. Database Migrations with Alembic

Alembic is used to track and apply changes to the database schema.
Applying Migrations
As mentioned in the setup, to apply all existing migrations to your database, run:

```bash
alembic upgrade head
```

This command will bring your database schema up to date with the latest version in the alembic/versions directory.
Creating a New Migration
Whenever you make a change to your models.py file (e.g., add a new table or a new column), you need to create a new migration script. Alembic can often detect these changes automatically.

```bash
alembic revision --autogenerate -m "A descriptive message about the changes"
```

After running this command:
Review the newly generated migration script in the alembic/versions/ folder to ensure it's correct.
Apply the migration to your database using the upgrade command shown above.

## Live Demo

The application is deployed and accessible at:

🔗 [https://todoapi-i777.onrender.com](https://todoapi-i777.onrender.com)

You can explore the interactive API documentation directly at:

📘 Swagger UI: [https://todoapi-i777.onrender.com/docs](https://todoapi-i777.onrender.com/docs)
