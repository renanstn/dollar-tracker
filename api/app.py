import os

from psycopg2 import pool
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://dollar-tracker.up.railway.app"])

DATABASE_URL = os.getenv("DATABASE_URL")
connection_pool = pool.SimpleConnectionPool(
    minconn=1, maxconn=10, dsn=DATABASE_URL
)

@app.route("/ping")
def ping():
    return "pong!"

@app.route("/")
def get_data():
    connection = connection_pool.getconn()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, datehour, value FROM dollar ORDER BY id"
            )
            rows = cursor.fetchall()
            values = []
            for row in rows:
                converted_value = int(row[2]) / 100
                values.append(
                    {
                        "datehour": row[1],
                        "value": converted_value,
                    }
                )
            return jsonify(values)
    finally:
        connection_pool.putconn(connection)


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
