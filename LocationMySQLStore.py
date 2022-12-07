from DBCon import DBCon
from Helper import Helper
from model import LocationModel
class LocationMySQLStore():
    dbCon = DBCon()
    helper = Helper()
    def __init__(self) -> None:#consturctor
        pass        

    def addLocationData(this, location, latitude, longitude):
        sql = "INSERT INTO locations (location, latitude, longitude) VALUES (%s, %s, %s)"
        val = (location, latitude, longitude)
        this.dbCon.insert(sql, val)
        return True

    def getLocationData(this, location):
        if(this.checkLocation(location)):
            sql = "SELECT latitude, longitude FROM locations where location = %s"
            val = (location,)
            data = this.dbCon.execute(sql, val)
            locationData = LocationModel()
            locationData.latitude = str(data[0][0])
            locationData.longitude = str(data[0][1])
            return locationData
        return None
    
    def listAllLocations(this):
        sql = "SELECT location from locations"
        data = this.dbCon.execute(sql)
        ret = []
        for x in data:
            ret.append(x[0])
        return ret
    
    def checkLocation(this, location):
        try:
            sql = "SELECT 1 FROM locations where location = %s;"
            val = (location,)
            data = this.dbCon.execute(sql, val)
            isPresent = False
            for i in data:
                isPresent = True
                break
            return isPresent
        except Exception as e:
            this.helper.log_error("checkLocation", e)
            return False

    