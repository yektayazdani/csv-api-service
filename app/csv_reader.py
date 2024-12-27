import pandas as pd
from app.data_model import CsvItem
import logging
from app.config import CSV_FILE_PATH
from app.utils import setup_logger

logger = setup_logger(__name__)

def read_csv_file():
    """Reads the CSV file and returns a list of CsvItem objects."""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        # Convert rows to dictionaries for the CsvItem constructor
        data_list = df.to_dict(orient='records')
        items = [CsvItem(data) for data in data_list]
        logger.info(f"Successfully read {len(data_list)} items from CSV file.")
        return items
    except FileNotFoundError:
        logger.error(f"CSV file not found at path: {CSV_FILE_PATH}")
        return []
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return []