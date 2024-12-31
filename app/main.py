from app.csv_reader import read_csv_file
from app.api_client import make_api_call
from app.config import CSV_FILE_PATH
import logging
from app.utils import setup_logger

logger = setup_logger(__name__)

def main():
    """Main function to read CSV and make API calls."""
    items = read_csv_file(CSV_FILE_PATH)
    if not items:
         logger.error("No items to process.")
         return
    for item in items:
       api_response = make_api_call(item.data)
       if api_response:
           logger.info(f"Successfully processed: {item.data}, response {api_response}")


if __name__ == "__main__":
    main()