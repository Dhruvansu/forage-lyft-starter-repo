from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import spindler_battery, nubbin_battery
from tires import carrigan_tires, octoprime_tires
from car import Car

class Car_factory():
    def __init__(self):
        self = self

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        capuletEngine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        tires = carrigan_tires(tire_wear)
        calliope = Car(capuletEngine, spindlerBattery, tires)
        return calliope

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        tires = carrigan_tires(tire_wear)
        glissade = Car(willoughbyEngine, spindlerBattery, tires)
        return glissade
    
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        sternamnEngine = sternman_engine.SternmanEngine(warning_light_on)
        spindlerBattery = spindler_battery.Spindler_battery(last_service_date, current_date)
        tires = octoprime_tires(tire_wear)
        palindrome = Car(sternamnEngine, spindlerBattery, tires)
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        willoughbyEngine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbin_battery.Nubbin_battery(last_service_date, current_date)
        tires = carrigan_tires(tire_wear)
        rorschach = Car(willoughbyEngine, nubbinBattery, tires)
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        capuletEngine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = nubbin_battery.Nubbin_battery(last_service_date, current_date)
        tires = octoprime_tires(tire_wear)
        thovex = Car(capuletEngine, nubbinBattery, tires)
        return thovex