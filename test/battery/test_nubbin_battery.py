import unittest
from datetime import date

from battery.nubbin_battery import Nubbin_battery


class test_capulet_engine(unittest.TestCase):
    def yes_needs_service(self):
        current_date = date.fromisoformat("03/22/2022")
        last_service_date = date.fromisoformat("03/22/2017")
        battery = Nubbin_battery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def no_needs_service(self):
        current_date = date.fromisoformat("03/22/2022")
        last_service_date = date.fromisoformat("03/22/2020")
        battery = Nubbin_battery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())