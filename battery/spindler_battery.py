from battery import Battery
from datetime import date

class Spindler_battery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        last_serviced_year = self.__current_date.replace(year=self.__current_date.year - 3)
        return last_serviced_year > self.__last_service_date.year