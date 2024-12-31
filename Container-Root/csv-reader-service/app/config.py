import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "data/input.csv")