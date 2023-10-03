from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan_tire import CarriganTire

class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = SpindlerBattery(last_service_date)
        glissade_tire = CarriganTire(tire_sensor_data)

        super().__init__(glissade_engine, glissade_battery, glissade_tire)

        self.engine = glissade_engine
        self.battery = glissade_battery
        self.tire = glissade_tire
    
    def needs_service(self):
        return super().needs_service()
