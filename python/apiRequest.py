import requests
import json

response = requests.get('https://api.open-meteo.com/v1/forecast?'
                        'latitude=46.7667&longitude=23.6'
                        '&daily=temperature_2m_max&daily=temperature_2m_min'
                        '&timezone=auto&daily=sunrise&daily=sunset'
                        '&daily=precipitation_probability_max'
                        '&daily=windspeed_10m_max')

response.raise_for_status()
if response.status_code == 200:
    print("Connection successfully established with the API. Status code:", response.status_code)

jsonData = json.loads(response.text)

file = open('data.json','w')
json.dump(jsonData, file)
file.close()