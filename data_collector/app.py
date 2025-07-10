import logging
import os
from datetime import datetime

import requests
from custom_types import DollarData
from database import Database
from dotenv import load_dotenv


class API:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    target_value = "bid"  # or "ask"?
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    @classmethod
    def get_data(cls) -> DollarData:
        """
        Load data from awesomeapi.
        Dollar value will be rounded, and transformed in a integer.
        """
        response = requests.get(f"{cls.url}?token={cls.api_key}")
        if response.status_code != 200:
            cls.logger.exception(f"API response was not 200: {response.text}")
            return
        data = response.json()
        timestamp = int(data["USDBRL"]["timestamp"])
        dollar_value_str = data["USDBRL"][cls.target_value]
        dollar_value = str(round(float(dollar_value_str), 2))
        dollar_value_int = int(dollar_value.replace(".", ""))
        return {"timestamp": timestamp, "dollar_value": dollar_value_int}
