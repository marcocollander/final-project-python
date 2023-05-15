import requests
from pprint import pprint

# https://api.nbp.pl/api/exchangerates/tables/a/
# https://api.nbp.pl/api/exchangerates/tables/b/
# https://api.nbp.pl/api/exchangerates/tables/c/


response = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/')
data = response.json()
# print(data[0]['rates'][1]['currency'])
# print(data[0]['rates'][1]['code'])
# print(data[0]['rates'][1]['mid'])

for item in data[0]['rates']:
    if item['code'] == 'USD':
        print(f"{item['mid']:.2f}")
    match item['code']:
        case 'USD':  print(f"{item['mid']:.2f}")
        case 'EUR':  print(f"{item['mid']:.2f}")
        case 'CHF':  print(f"{item['mid']:.2f}")
