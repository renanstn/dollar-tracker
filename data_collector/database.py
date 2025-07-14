import os
import sqlite3
from datetime import datetime

import psycopg2
from dotenv import load_dotenv
from sql_queries import (
    create_table_query_postgres,
    create_table_query_sqlite,
    insert_values_query_postgres,
    insert_values_query_sqlite,
    get_last_datehour_query_postgres,
)


class Database:
    def __init__(self):
        load_dotenv()
        database_url = os.getenv("DATABASE_URL")
        if database_url.startswith("postgres"):
            self.db = "postgres"
            self.connection = psycopg2.connect(database_url)
            self.cursor = self.connection.cursor()
        else:
            self.db = "sqlite"
            self.connection = sqlite3.connect(database_url)
            self.cursor = self.connection.cursor()

    def create_table(self):
        if self.db == "sqlite":
            self.cursor.execute(create_table_query_sqlite)
        else:
            self.cursor.execute(create_table_query_postgres)
            self.connection.commit()

    def load_values(self, datetime: datetime, value: int):
        if self.db == "sqlite":
            self.cursor.execute(
                insert_values_query_sqlite, (datetime.isoformat(), value)
            )
            self.connection.commit()
        else:
            self.cursor.execute(
                insert_values_query_postgres, (datetime, value)
            )  # passa datetime como objeto
            self.connection.commit()

    def get_last_datehour(self):
        self.cursor.execute(get_last_datehour_query_postgres)
        rows = self.cursor.fetchall()
        if not rows:
            return []
        return rows[0][0]
