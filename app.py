'''Date: 6 July 2020
Author: Justin Beaurone
Purpose: Demonstrate a simple server-side API implementation.
'''
import connexion


def fetch_price(asset):
    # we use this function to do whatever it is our api offers.

    return { asset: 4.85 } # returning a dict - this becomes the json response

# connexion handles routing using the specifications document
app = connexion.App(__name__)
app.add_api('swagger_example.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
