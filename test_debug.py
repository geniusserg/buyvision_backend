# run server (python3 app.py)!!!
# run tests (pytest test.py)

import pytest 
import requests
from app import *

def test_crem():
    product = getClient().get('gtin?gtin=4607092074702').text
    assert  'Стоп проблема' in product