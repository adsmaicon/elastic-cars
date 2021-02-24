from src.repository.car_repository import CarRepository

class CarController:
    
    def store(self, data):
        try:
            return CarRepository().store(data)
        except Exception:
            return 'Missing Params', 422
