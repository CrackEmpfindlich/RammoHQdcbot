import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
"user": os.getenv("DB_USER"),
"password": os.getenv("DB_PASSWORD"),
"database": os.getenv("DB_NAME"),
"host": os.getenv("DB_HOST")
}

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
