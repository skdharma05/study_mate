# Student Management System Backend

This is the backend service for the Student Management System, built with FastAPI and SQLAlchemy.

## Features

- RESTful API for student management
- MySQL database integration using SQLAlchemy
- Environment configuration with python-dotenv
- Async server with Uvicorn

## Requirements

- Python 3.10+
- MySQL server
- See [pyproject.toml](backend/pyproject.toml) for dependencies

## Setup

1. **Clone the repository**
2. **Create a virtual environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   Or use pyproject.toml with your preferred tool.

4. **Configure MySQL**
   - Ensure MySQL is running and accessible.
   - Create a database for the project.
   - Update your `.env` file with MySQL connection details:
     ```
     DATABASE_URL=mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>
     ```

## Running the Backend

```sh
cd backend/app
python main.py
```

Or, to run with Uvicorn and FastAPI:

```sh
uvicorn app.main:main --reload
```