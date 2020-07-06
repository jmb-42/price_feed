'''Date: 6 July 2020
Author: Justin Beaurone
Purpose: Demonstrate a simple server-side API implementation.
'''
import connexion


ASSET_PRICES = {
    'LINKUSD': 4.85,
    'ETHBTC': 0.02570556,
    'BTCUSD': 9284.68,
    'ETHUSD': 238.48
    }

def fetch_price(asset):
    # we use this function to do whatever it is our api offers.
    # returning a python dictionary becomes serialized json

    # successful calls are only for assets we have pricing data for
    if asset in ASSET_PRICES.keys():
        return { asset: ASSET_PRICES[asset] }, 200
    else:
        return { "message": "{} data not available".format(asset) }, 404

def fetch_pairs():
    return {'tradingPairs': [ pair for pair in ASSET_PRICES.keys() ] } 

# connexion handles routing using the specifications document
app = connexion.App(__name__)
app.add_api('swagger_example.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
