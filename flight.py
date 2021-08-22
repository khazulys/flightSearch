import requests

def airport(api_key, city):
	url = f'https://api.flightapi.io/iata/{api_key}/{city}/airport'
	resp = requests.get(url)
	data = resp.json()
	for airports in data["data"]:
		for key, value in airports.items():
			print(key,':',value)

airport('611fc8a1747a9a0532560f11','batam')

def searchAirlines(api_key, departure, arrival, date):
	url = f'https://api.flightapi.io/onewaytrip/{api_key}/{departure}/{arrival}/{date}/1/0/0/Economy/USD'
	resp = requests.get(url)
	data = resp.json()
	for result in data['airlines']:
		for key, value in result.items():
			print(key,':',value)

searchAirlines(api_key = '611fc8a1747a9a0532560f11',
	departure = 'bth'.upper(),
	arrival = 'kno'.upper(),
	date = '2021-08-24')
