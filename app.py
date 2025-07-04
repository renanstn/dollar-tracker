import os
import sqlite3
from datetime import datetime
from typing import TypedDict

import requests
from dotenv import load_dotenv


class Database:
    """
    TODO: Adapt for postgres.
    """
    load_dotenv()
    connection = sqlite3.connect(os.getenv("DATABASE_URL"))
    cursor = connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dollar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datehour TEXT NOT NULL,
                value INTEGER NOT NULL
            )
        """)

    def load_values(self, datetime, value):
        self.cursor.execute("""
            INSERT INTO dollar (datehour, value)
            VALUES (?, ?)
        """, (datetime.isoformat(), value))
        self.connection.commit()


class DollarData(TypedDict):
    timestamp: int
    dollar_value: int


class API:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    target_value = "bid"  # or "ask"?

    @classmethod
    def get_data(cls) -> DollarData:
        """
        Load data from awesomeapi.
        Dollar value will be rounded, and transformed in a integer.
        """
        response = requests.get(f"{cls.url}?token={cls.api_key}")
        if response.status_code != 200:
            # TODO: Report error
            return
        data = response.json()
        timestamp = int(data["USDBRL"]["timestamp"])
        dollar_value_str = data["USDBRL"][cls.target_value]
        dollar_value = str(round(float(dollar_value_str), 2))
        dollar_value_int = int(dollar_value.replace(".", ""))
        return {"timestamp": timestamp, "dollar_value": dollar_value_int}

# Test area -------------------------------------------------------------------
test = API()
database = Database()

data = test.get_data()
print(data)

datetime = datetime.fromtimestamp(int(data["timestamp"]))

database.create_table()
database.load_values(datetime, data["dollar_value"])
