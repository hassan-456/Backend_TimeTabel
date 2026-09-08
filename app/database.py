import os
from pathlib import Path

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# Always load .env from the backend project root (not from wherever uvicorn was started)
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URL:
    raise ValueError(f"MONGODB_URL is not set. Expected .env at: {ENV_PATH}")

if not DATABASE_NAME:
    raise ValueError(f"DATABASE_NAME is not set. Expected .env at: {ENV_PATH}")

# Use certifi CA bundle so TLS works reliably on Windows
client = MongoClient(
    MONGODB_URL,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000,
)

db = client[DATABASE_NAME]


def check_connection() -> bool:
    """Ping MongoDB and print a clear success/failure message."""
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
        print(f"Database: {DATABASE_NAME}")
        return True
    except (ServerSelectionTimeoutError, ConnectionFailure) as e:
        error_text = str(e)
        print("MongoDB connection failed!")
        print(f"Error: {error_text[:300]}")
        if "SSL" in error_text or "TLS" in error_text or "timed out" in error_text.lower():
            print(
                "\nLikely cause: your IP is not allowed in MongoDB Atlas Network Access.\n"
                "Fix steps:\n"
                "  1. Open https://cloud.mongodb.com\n"
                "  2. Go to your project → Network Access\n"
                "  3. Click 'Add IP Address'\n"
                "  4. Choose 'Add Current IP Address' (or temporarily 'Allow Access from Anywhere' 0.0.0.0/0)\n"
                "  5. Wait 1–2 minutes, then restart the backend\n"
            )
        return False
    except Exception as e:
        print("MongoDB connection failed!")
        print(f"Unexpected error ({type(e).__name__}): {e}")
        return False


# Run check when this module is imported (app startup)
check_connection()
