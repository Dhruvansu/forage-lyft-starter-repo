import unittest

from engine.capulet_engine import CapuletEngine


class test_capulet_engine(unittest.TestCase):
    def yes_needs_service(self):
        current_mileage = 50000
        last_service_mileage = 15000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def no_needs_service(self):
        current_mileage = 50000
        last_service_mileage = 49000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())