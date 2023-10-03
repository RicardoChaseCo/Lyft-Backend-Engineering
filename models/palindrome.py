from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire

class Palindrome(Car):
    def __init__(self, last_service_date, warning_indicator_on, tire_sensor_data):
        palindrome_engine = SternmanEngine(warning_indicator_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        palindrome_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(palindrome_engine, palindrome_battery, palindrome_tire)

        self.engine = palindrome_engine
        self.battery = palindrome_battery
        self.tire = palindrome_tire
    
    def needs_service(self):
        return super().needs_service()
