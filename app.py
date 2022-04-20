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
def searchProductByGtin():
    gtin = request.args.get('gtin')
    listProducts = methods.getProducts(gtin)
    return json.dumps(listProducts.__dict__, ensure_ascii=False, default=lambda o: o.__dict__)

@app.route('/search/google', methods=['GET'])
def searchGoogle():
    data = request.args.get('data')
    if request.args.get('type') == 'text':
        pass
    elif request.args.get('type') == 'gtin':
        pass
    else:
        pass
    return data

@app.route('/search/sbermarket', methods=['GET'])
def searchSber():
    data = request.args.get('data')
    return data

@app.route('/search/yamarket', methods=['GET'])
def searchYamarket():
    data = request.args.get('data')
    return data

def getClient():
    app.run()
    return app.test_client()

if __name__ == "__main__":
    app.run()
    