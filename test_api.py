'''Date: 6 July 2020
Author: Justin Beaurone
Purpose: Demonstrate a simple client-side use of our API.
'''
import json
import requests


API_BASE_URL = 'http://0.0.0.0:8080/' # base path of the api
PRICE_FEED = API_BASE_URL + 'price'   # price feed endpoint

params = {
    'asset': 'LINKUSD' # request the price of Chainlink, in units of USD
    }

# client sends a get request with the given parameters
r = requests.get(PRICE_FEED, params=params)

# client does whatever they want with the result. we just display it
print( json.dumps(r.json(), indent=4) )
