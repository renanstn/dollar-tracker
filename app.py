import os

import requests
from dotenv import load_dotenv


class API:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    target_value = "bid"  # or "ask"?

    @classmethod
    def get_value(cls) -> float:
        response = requests.get(f"{cls.url}?token={cls.api_key}")
        if response.status_code != 200:
            return
        data = response.json()
        dollar_value_str = data["USDBRL"][cls.target_value]
        dollar_value = round(float(dollar_value_str), 2)
        return dollar_value

# -----------------------------------------------------------------------------
test = API()
value = test.get_value()
print(value)
