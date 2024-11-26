import os
from dotenv import load_dotenv
from fastapi import FastAPI
from .routes import user
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, Request, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from pymongo import MongoClient
from bson import json_util
import json

app = FastAPI()
load_dotenv()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)

# General exception handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred. Please try again later.",
            "error": str(exc)
            },
    )

# Example of a specific exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
    
    
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/all")
def get_all():
    
    try:
        DATABASE_URL = os.getenv('DATABASE_URL')
        client = MongoClient(DATABASE_URL)
        db = client[os.getenv("DATABASE_NAME")]
        firstCollection = db.list_collection_names()[0]
        collection = db[firstCollection]
        documents = collection.find()
        # documents_list = list(documents)  # Convert cursor to list
        # documents_json = json_util.dumps(documents_list)  # Convert to JSON
        return documents
    except Exception as e:
        return {'message': 'Connection failed!', 'error': str(e)}
    