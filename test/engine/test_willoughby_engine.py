import unittest

from engine.willoughby_engine import WilloughbyEngine


class test_willoughby_engine(unittest.TestCase):
    def yes_needs_service(self):
        current_mileage = 80000
        last_service_mileage = 25000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def no_needs_service(self):
        current_mileage = 80000
        last_service_mileage = 69000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())