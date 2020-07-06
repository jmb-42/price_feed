'''Date: 6 July 2020
Author: Justin Beaurone
Purpose: Demonstrate a simple client-side use of our API.
'''
import json
import requests


API_BASE_URL = 'http://0.0.0.0:8080/' # base path of the api
PRICE_FEED = API_BASE_URL + 'price'   # price feed endpoint
PAIRS = API_BASE_URL + 'pairs'        # pairs endpoint

# client sends a get request to receive all trading pairs
r = requests.get(PAIRS)
# display the trading pairs to the terminal
print( 'Querying for all trading pairs using URL:\n{}'.format(r.url) )
print( json.dumps(r.json(), indent=4) )

# Get the list of pairs from the json dictionary
tradingPairs = r.json()['tradingPairs'] + ['BTCUSDT']

# query the API for multiple trading pairs and print the result
for pair in tradingPairs:
    r = requests.get(PRICE_FEED, params={'asset': pair})
    print( 'Querying for {} price data using URL:\n{}'.format(pair, r.url) )
    print( json.dumps(r.json(), indent=4) )
