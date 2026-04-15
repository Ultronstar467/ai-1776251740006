from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) to allow frontend to access
origins = [
    "http://localhost",
    "http://localhost:8000",  # FastAPI default port
    "http://localhost:5500",  # Common for Live Server VS Code extension
    "http://127.0.0.1:5500",  # Another common Live Server address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Calculator API! Use /add, /subtract, /multiply, /divide endpoints."}

@app.get("/add")
async def add_numbers(num1: float, num2: float):
    """Adds two numbers."""
    try:
        result = num1 + num2
        return {"operation": "add", "num1": num1, "num2": num2, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")

@app.get("/subtract")
async def subtract_numbers(num1: float, num2: float):
    """Subtracts num2 from num1."""
    try:
        result = num1 - num2
        return {"operation": "subtract", "num1": num1, "num2": num2, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")

@app.get("/multiply")
async def multiply_numbers(num1: float, num2: float):
    """Multiplies two numbers."""
    try:
        result = num1 * num2
        return {"operation": "multiply", "num1": num1, "num2": num2, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")

@app.get("/divide")
async def divide_numbers(num1: float, num2: float):
    """Divides num1 by num2, handles division by zero."""
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    try:
        result = num1 / num2
        return {"operation": "divide", "num1": num1, "num2": num2, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {e}")

# To run this FastAPI application, save it as main.py and execute:
# uvicorn main:app --reload --port 8000
# Then open index.html in your browser (e.g., via Live Server).