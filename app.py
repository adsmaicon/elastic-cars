from flask import Flask
from elasticsearch import Elasticsearch
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    es = Elasticsearch(
        [os.getenv("HOST")],
        http_auth=(
            os.getenv("USER"), 
            os.getenv("PASS")
        ),
        scheme="https",
        port=443,
    )

    car = {
        "modelo": "chevete do xostack",
        "placa": "XOS-1814"
    }

    es.index(index='cars', id=1, body=car)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
