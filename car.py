from serviceable import *


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery

    @abstractmethod
    def needs_service(self):
        pass
