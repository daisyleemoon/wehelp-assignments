import urllib.request
import csv
import json
import re

with urllib.request.urlopen(
		"https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json") as url:
	data_json = json.loads(url.read().decode())

attractions_data = data_json["result"]["results"]

data = open('data.csv', 'w', newline='', encoding="utf-8")
csv_writer = csv.writer(data)

for attraction in attractions_data:
	stitle = attraction["stitle"]
	longitude = attraction["longitude"]
	latitude = attraction["latitude"]
	file = attraction["file"]
	img_url = re.split(r"(?i)\.JPG", file)[0] + ".jpg"
	address = attraction["address"][5] + attraction["address"][6] + attraction["address"][7]
	attractions_info = [stitle, address, longitude, latitude, img_url]

	csv_writer.writerow(attractions_info)

data.close()
