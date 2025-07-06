FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY \
	app.py \
	create_database.py \
	custom_types.py \
	database.py \
	run_get_data.py \
	sql_queries.py \
	.
CMD ["python", "run_get_data.py"]
