FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py custom_types.py database.py sql_queries.py .
CMD ["python", "app.py"]
