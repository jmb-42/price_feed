# price_feed
A simple example to demonstrate using connexion to offer a RESTful API.

## Installation

Using `venv` and `pip`:

        git clone https://www.github.com/jmb-42/price_feed
        cd price_feed
        python3 -m venv api_env
        source api_env/bin/activate
        pip install -r requirements.txt

## Run the Code

Launch the server using `python app.py`. You can navigate to
http://0.0.0.0:8080/ui in your browser to test the API. Or, you
can use another terminal to run `test_api.py`.

## swagger_example.yaml

This file was written before the python code. It details the specifications
of the API. Using this approach, I had a well-defined structure to develop the
server code, and now we can use this file to provide documentation on the
services offered by the API.
