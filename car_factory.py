from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import spindler_battery, nubbin_battery
from car import Car

class Car_factory():
    def __init__(self):
        self = self

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        calliope = Car(capuletEngine, spindlerBattery)
        return calliope

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        glissade = Car(willoughbyEngine, spindlerBattery)
        return glissade
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternamnEngine = sternman_engine.SternmanEngine(warning_light_on)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        palindrome = Car(sternamnEngine, spindlerBattery)
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbin_battery.Nubbin_battery(last_service_date, current_date)
        rorschach = Car(willoughbyEngine, nubbinBattery)
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capuletEngine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbin_battery.Nubbin_battery(last_service_date, current_date)
        thovex = Car(capuletEngine, nubbinBattery)
        return thovex