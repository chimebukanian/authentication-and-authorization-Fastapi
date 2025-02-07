from fastapi import FastAPI
from database import init_db
import user

app = FastAPI(title="FastAPI Auth API")

# Initialize Database
init_db()

# Include Routes
app.include_router(user.router)
