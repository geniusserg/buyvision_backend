#!/usr/bin/python3

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import sqlalchemy
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import methods
import json

app = Flask(__name__)
app.config["TESTING"] = True

@app.route('/gtin', methods=['GET'])
def index():
    gtin = request.args.get('gtin')
    listProducts = methods.getProducts(gtin)
    return json.dumps(listProducts.__dict__, ensure_ascii=False, default=lambda o: o.__dict__)

def getClient():
    app.run()
    return app.test_client()

if __name__ == "__main__":
    app.run()
    