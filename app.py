import json
from flask import Flask, request
from Helper import Helper
from LocationMongoDBStore import LocationMongoDBStore


app = Flask(__name__)

locationStore = LocationMongoDBStore()
helper = Helper()

@app.route("/weather_details", methods=["GET"])
def weather():
    try:
        args = request.args
        location = args.get('location')
        if location == "":
            return "Provide location in request", 400
        location = location.lower()
        if locationStore.checkLocation(location):
            data = locationStore.getLocationData(location)
            if data != None:
                weather = helper.weather_details(data.latitude, data.longitude)
            else:
                return "Could not fetch location details. Please try again"
            if weather != None:
                return weather, 200
            return "Could not fetch Weather details, please try again!", 500
        else:
            return "Location is not present in database, enter one of the following locations\n" + ",".join(locationStore.listAllLocations()), 200
    except Exception as e:
        helper.log_error("weather", e)
        return "something went wrong", 500

@app.route("/weather_ip", methods=["GET"])
def ipweather():
    try:
        args = request.args
        ip_address = args.get("ip_address")
        if not helper.validate_ip_address(ip_address):
            return "Invalid IP Address", 400
        else:
            location = helper.location_details_ip(ip_address)
            if(location != None):
                weather = helper.weather_details(location.latitude, location.longitude)
                if weather != None:
                    return weather, 200
            return "Could not fetch Weather details, please try again!", 500
    except Exception as e:
        helper.log_error("ipweather", e)
        return "Something went wrong", 500

@app.route("/add_location", methods=["PUT"])
def adding_location():
    try:
        locationData = json.loads(request.data)
        for data in locationData:
            locationStore.addLocationData(
                data["location"], data["latitude"], data["longitude"])
        return "Successfully Added Locations", 200
    except Exception as e:
        helper.log_error("adding_location", e)
        return "Something went wrong", 500


@app.route("/", methods=["GET"])
def home():
    return "Welcome to Weather Project. Please use our APIs to get weather details", 200


if __name__ == "__main__":
    app.run(debug=True)
