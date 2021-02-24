from elasticsearch import Elasticsearch
import uuid
import os

class CarRepository:

    def __init__(self):
        self.es = Elasticsearch(
            [os.getenv("HOST")],
            http_auth=(
                os.getenv("USER"), 
                os.getenv("PASS")
            ),
            scheme="https",
            port=443,
        )

    def store(self, data):
        car_data = {
            'placa': data['placa'],
            'marca': data['marca'],
            'modelo': data['modelo'],
            'cor': data['cor'],
            'ano': data['ano'],
            'combustivel': data['combustivel'],
            'status': 'disponivel'
        }
        id = str(uuid.uuid4())

        self.es.index(index='cars', id=id, body=car_data)

        car_data['id'] = id
        return car_data