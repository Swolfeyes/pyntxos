import json

data = [
  {"name": "Argotia",
  "latitude": 43.2590929,
  "longitude": -2.9244257,
  "address": "Plaza Nueva, 48005 Bilbao, Vizcaya, Spain"},
 {"name": "Sorginzulo",
  "latitude": 43.259387,
  "longitude": -2.9233905,
  "address": "Plaza Nueva, 12, 48005 Bilbao, BI, Spain"}
]

with open('data/bilbao_restaurants2.json', 'w') as file:
    file.write(json.dumps(data, indent=4))
