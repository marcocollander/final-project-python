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
    match item['code']:
        case 'USD':  rate = f"{item['mid']:.2f}"
        case 'EUR':  rate = f"{item['mid']:.2f}"
        case 'CHF':  rate = f"{item['mid']:.2f}"
        case _: rate = None
