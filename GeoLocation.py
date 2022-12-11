from geopy.geocoders import Nominatim
loc = Nominatim(user_agent="GetLoc")
def getGeoLocation(locaName:str)->tuple:
    __geoLoc = loc.geocode(locaName)
    return (__geoLoc.latitude,__geoLoc.longitude)
