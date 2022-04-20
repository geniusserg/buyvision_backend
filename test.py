# run server (python3 app.py)!!!
# run tests (pytest test.py)

import pytest 
import requests

def test_crem():
    product = requests.get('http://localhost:5000/gtin?gtin=4607092074702').text
    assert  'Стоп проблема' in product