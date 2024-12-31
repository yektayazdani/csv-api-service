import requests
from app.config import API_URL
from app.utils import setup_logger

logger = setup_logger(__name__)

def make_api_call(item_data):
    """Makes an API call to the external service."""
    try:
        response = requests.post(API_URL, json=item_data)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        logger.info(f"API call successful for data: {item_data}")
        return response.json()
    except requests.exceptions.RequestException as e:
         logger.error(f"Error during API call for data {item_data}: {e}")
         return None