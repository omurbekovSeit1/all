import requests
from config import API
sity = input('City: ')
try:
    a = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={sity}&appid={API}&units=metric'
    )
    print(a)
except Exception as ex:
    print(ex)
    print('correct City!!!!!')