import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://dollar-tracker.up.railway.app"])

DATABASE_URL = os.getenv("DATABASE_URL")
connection = psycopg2.connect(DATABASE_URL)


@app.route("/")
def get_data():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, datehour, value FROM dollar ORDER BY id")
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


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
