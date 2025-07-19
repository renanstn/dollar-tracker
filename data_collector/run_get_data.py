from datetime import datetime

import pytz
from app import API
from database import Database
from psycopg2 import errors

collector = API()
database = Database()

data = collector.get_data()
tz = pytz.timezone("America/Sao_Paulo")
datetime_utc = datetime.fromtimestamp(int(data["timestamp"]))
datetime_with_timezone = pytz.utc.localize(datetime_utc).astimezone(tz)
try:
	database.load_values(datetime_with_timezone, data["dollar_value"])
except errors.UniqueViolation:
	database.connection.rollback()
	exit()
