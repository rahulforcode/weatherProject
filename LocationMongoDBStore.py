import pymongo
from model import LocationModel

class LocationMongoDBStore():
    __client = ""
    __locations = ""
    def __init__(self) -> None:#constructor
        self.__client = pymongo.MongoClient("<clienttURL>")
        db = self.__client.weatherproject
        self.__locations = db.locations

    def addLocationData(this, location, latitude, longitude) -> bool:
        if not this.checkLocation(location):
            locationDic = {"location":location , "latitude": latitude, "longitude": longitude }
            this.__locations.insert_one(locationDic)
        return True

    def getLocationData(this, location) -> LocationModel:
        if(this.checkLocation(location)):
            locationResponse = this.__locations.find_one({"location":location})

            locationData = LocationModel()
            locationData.latitude = locationResponse["latitude"]
            locationData.longitude = locationResponse["longitude"]
            return locationData
        return None
    
    def listAllLocations(this):
        data = this.__locations.find()
        ret = []
        for x in data:
            ret.append(x["location"])
        return ret
    
    def checkLocation(this, location):
        count = this.__locations.count_documents({"location":location})
        return count != 0
