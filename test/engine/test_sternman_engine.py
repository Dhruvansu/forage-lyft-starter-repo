from tkinter import W
import unittest

from engine.sternman_engine import SternmanEngine


class test_sternman_engine(unittest.TestCase):
    def yes_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def no_needs_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())