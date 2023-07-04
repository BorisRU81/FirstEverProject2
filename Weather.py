import requests  #библиотека для HTTP запросов
from datetime import datetime

town = input('Введите Город')

key = '3e5fdfa69cd6507d5c6256e689b86256'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': town, 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()

print(result)

data = result['main']

print(f'Координаты: {result["coord"]["lon"]}, {result["coord"]["lat"]}')
print(f'Температура: {data["temp"]:.1f}\xB0C')
