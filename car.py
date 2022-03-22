from serviceable import *


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.__engine = engine
        self.__battery = battery
        self.__tires = tires

    def needs_service(self):
        pass
