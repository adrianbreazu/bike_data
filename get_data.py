import requests
import json
import datetime
import sqlite3

url = 'http://portal.clujbike.eu/Station/Read?Grid-sort=StationName-asc'
response = requests.post(url)
json_data = json.dumps(response.text)
datetime=datetime.datetime.now()


con = sqlite3.connect('/your/path/here/clujbike-script/db/clujbike.db')

c = con.cursor()
c.execute("INSERT INTO data VALUES(NULL, ?,?);", (json_data, datetime))
con.commit()

print("done time: {0}".format(datetime))
