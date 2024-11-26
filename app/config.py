from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://mongo_db:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "traffic_detection")

settings = Settings()