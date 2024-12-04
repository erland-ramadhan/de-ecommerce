import pandas as pd
import requests
import logging

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_csv(file_path):
    try:
        logger.info(f"Extracting data from CSV: {file_path}")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        logger.error(f"Error while reading CSV: {e}")
        raise

def extract_api(api_url, headers=None):
    try:
        logger.info(f"Fetching data from API: {api_url}")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error while fetching API data: {e}")
        raise

