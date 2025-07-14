from datetime import datetime

import pytz
from app import API
from database import Database

collector = API()
database = Database()

data = collector.get_data()
tz = pytz.timezone("America/Sao_Paulo")
datetime_utc = datetime.fromtimestamp(int(data["timestamp"]))
datetime_with_timezone = pytz.utc.localize(datetime_utc).astimezone(tz)

last_datehour = database.get_last_datehour()
if last_datehour and datetime_with_timezone == datetime.fromisoformat(
    last_datehour
):
    exit()
database.load_values(datetime_with_timezone, data["dollar_value"])
