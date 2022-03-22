import unittest

from tires.carrigan_tires import Carrigan_tires

class test_carrigan_tires(unittest.TestCase):
    def yes_needs_service(self):
        tire_wear = [0.6, 0.7, 0.5, 0.9]
        tires = Carrigan_tires(tire_wear)
        self.assertTrue(tires.needs_service())

    def no_needs_service(self):
        tire_wear = [0.6, 0.5, 0.4, 0.8]
        tires = Carrigan_tires(tire_wear)
        self.assertFalse(tires.needs_service())