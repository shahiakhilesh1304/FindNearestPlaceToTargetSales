import Imports as im

def targetCityCoOrdinates(cityName:str)->tuple:
    return im.coordinate.getGeoLocation(cityName)