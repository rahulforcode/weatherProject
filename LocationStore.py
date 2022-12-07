from model import LocationModel
class LocationStore():
    __locationDic = {}

    def __init__(self) -> None:#consturctor
        self.__locationDic =  {"secunderabad": {"latitude": "17", "longitude": "78"}, 
                "bangalore": {"latitude": "12", "longitude": "77"}, 
                "kalanjoor": {"latitude": "9", "longitude": "76"}}

    def addLocationData(this, location, latitude, longitude):
        this.__locationDic[location] = {"latitude" : latitude, "longitude" : longitude}
    
    def getLocationData(this, location):
        if(location in this.__locationDic):
            locationData = LocationModel()
            locationData.latitude = this.__locationDic[location]["latitude"]
            locationData.longitude = this.__locationDic[location]["longitude"]
            return locationData
        return None
    
    def listAllLocations(this):
        return this.__locationDic.keys()
    
    def checkLocation(this, location):
        return location in this.__locationDic

