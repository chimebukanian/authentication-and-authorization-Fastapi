FastAPI Authentication API with JWT

A simple user authentication API built with FastAPI, JWT (JSON Web Tokens), SQLAlchemy, and Pydantic for secure authentication. This API allows user registration, login, and access to protected routes using JWT authentication.

Features

✅ User Registration (stores user info securely)✅ User Login (returns JWT for authentication)✅ Protected Endpoint (/user/profile) – Requires JWT✅ Password Hashing (using Passlib)✅ Uses SQLAlchemy + SQLite

📌 Technologies Used

FastAPI (for building the API)

SQLAlchemy (ORM for database management)

SQLite (lightweight database)

JWT Authentication (using PyJWT)

Passlib (for password hashing)

Pydantic (for request validation)

🚀 Getting Started

1. Prerequisites

Make sure you have the following installed:

Python 3.10+

FastAPI

SQLite (bundled with Python)

2. Clone the Repository

git clone https://github.com/yourusername/FastAPI-Auth.git
cd FastAPI-Auth

3. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

4. Run the API

uvicorn main:app --reload

The API will be available at:

Swagger UI → http://127.0.0.1:8000/docs

Redoc UI → http://127.0.0.1:8000/redoc

Base API URL → http://127.0.0.1:8000/api

📌 API Endpoints

1. Register a User

Endpoint: POST /auth/registerRequest Body (JSON):

{
  "username": "john_doe",
  "password": "password123"
}

Response:

{
  "message": "User registered successfully"
}

2. User Login

Endpoint: POST /auth/loginRequest Body (JSON):

{
  "username": "john_doe",
  "password": "password123"
}

Response (JWT Token):

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR...",
  "token_type": "bearer"
}

3. Get User Profile (Protected)

Endpoint: GET /user/profile
Headers:

Authorization: Bearer YOUR_JWT_TOKEN

Response:

{
  "message": "Welcome john_doe, this is your profile!"
}

⛔ If token is missing or invalid, the API returns:

{
  "detail": "Not authenticated"
}

📌 Environment Variables

To store your JWT secret key securely, create a .env file and add:

SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

🛠 How to Extend the Project

🚀 Here are some ways to improve this project:

Add Role-Based Authorization (Admin/User roles)

Integrate Refresh Tokens

Use PostgreSQL or MySQL instead of SQLite

Deploy to AWS/GCP/Azure

📜 License

This project is MIT Licensed – Feel free to use and modify it!

📞 Need Help?

For issues or improvements, open an issue on GitHub.


