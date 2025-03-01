# Aqua Home Assignment
This is a simple **FastAPI-based project** that allows you to manage users. It includes basic user creation, validation, and listing functionality.

## Requirements
Before running the project, make sure you have Python 3.7+ installed. You can check your Python version by running:
python --version

The required dependencies for this project are:

fastapi: A modern web framework for building APIs with Python 3.7+.
uvicorn: An ASGI server used to serve the FastAPI app.
pydantic: A data validation and settings management library used for validating incoming request data.
pytest (optional): A testing framework for running tests.

## Installation

1. Clone the repository to your local machine:
   git clone https://github.com/NadavElgrabli/Aqua-Home-Assignment.git
   cd Aqua-Home-Assignment

2. Create a virtual environment (optional but recommended):
   python -m venv venv

3. Activate the virtual environment:

### For Windows:
.\venv\Scripts\activate

### For macOS/Linux:
source venv/bin/activate

4. Install the required dependencies:

Run the following command to install FastAPI, Uvicorn, Pydantic, and pytest (optional for testing):
pip install fastapi uvicorn pydantic pytest

## Running the Application on Linux

1. Start the application with Uvicorn:
   To launch the server on a Linux machine, run the following command from the project root directory:

uvicorn backend.main:app --reload

This will start the FastAPI server on http://127.0.0.1:8000 by default. The --reload flag will automatically restart the server when you make changes to your code.

2. Access the API documentation:
   Once the server is running, you can access the automatic API documentation provided by FastAPI at:
http://127.0.0.1:8000/docs

This page allows you to interact with the API directly, make requests, and test the endpoints.

#### API Endpoints:
POST /users
Description: Adds a new user.
Request body (JSON):
{
"ID": "316082791",
"PhoneNumber": "0544340611",
"Name": "Nadav Erez Elgrabli",
"Address": "Tel Aviv"
}
Response:
200 OK: User successfully added.
400 Bad Request: If the Israeli ID or phone number is invalid or already in use.

GET /users
Description: Gets a list of all user names.
Response (JSON):
{
"users": ["Rachel Green", "Ross Geller", "Monica Geller", "Chandler Bing", "Joey Tribbiani", "Phoebe Buffay"]
}

GET /users/{name}
Description: Get a user by their name.
Response:
200 OK: Returns user details if found.
404 Not Found: If the user with that name is not found.

## Running Tests
To run the tests for this project, follow these steps:

1. Install the test dependencies (if not already installed):
   pip install pytest

2. Run the tests: to run the tests, execute the following command in the project directory:
   python -m pytest backend/test_main.py
   This will run all the tests in the test_main.py file.

## Project Structure
The project is organized as follows:
Aqua-Home-Assignment/
│
├── backend/
│   ├── main.py           # FastAPI app and routes
│   ├── models.py         # Pydantic models
│   ├── data_handler.py   # Handles data loading and saving
│   ├── test_main.py      # Test file for FastAPI endpoints
│   └── validation.py     # Validation logic for ID and phone numbers
│
├── requirements.txt      # Dependencies file (optional, for production environments)
├── users.json            # File to persist user data (optional)
└── README.md             # This file
