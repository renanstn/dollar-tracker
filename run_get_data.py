from datetime import datetime

from app import API
from database import Database

collector = API()
database = Database()

data = collector.get_data()
datetime = datetime.fromtimestamp(int(data["timestamp"]))
database.load_values(datetime, data["dollar_value"])
