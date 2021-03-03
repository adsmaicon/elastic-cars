from flask import Flask, request
from src.controller.car_controller import CarController

app = Flask(__name__)


@app.route('/car', methods=["POST"])
def car():
    data = request.json
    car_controller = CarController()
    return car_controller.store(data)


@app.route('/car/<id>', methods=["GET"])
def find(id):
    car_controller = CarController()
    return car_controller.findById(id)


if __name__ == '__main__':
    app.run()
