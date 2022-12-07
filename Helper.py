import ipaddress 
import requests
from datetime import datetime
from model import LocationModel
class Helper():

    def validate_ip_address(this, address):
        try:
            ip = ipaddress.ip_address(address)
            return True
        except ValueError:
            this.log_error("validate_ip_address", "IP address {} is not valid".format(address))
            return False

    def location_details_ip(this, ip_address):
        try:
            url = f"https://ipapi.co/{ip_address}/json/"
            res = requests.get(url = url)
            if(res):
                data = res.json()
                locationData = LocationModel()
                locationData.latitude = data["latitude"]
                locationData.longitude = data["longitude"]
                return locationData
            this.log_error("location_details_ip", str(res) + res.content)
            return None
        except Exception as e:
            this.log_error("location_details_ip", e)
            return None

    def weather_details(this, latitude, longitude):
        try:
            base_url = "https://api.open-meteo.com/v1/forecast"
            query = f"?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=relativehumidity_2m"
            url = base_url + query
            resp = requests.get(url=url)
            if(resp):
                meteoData = resp.json()
                ret = {}
                ret["temperature"] = meteoData["current_weather"]["temperature"]
                ret["time"] = meteoData["current_weather"]["time"]
                ret["humidity"] = meteoData["hourly"]["relativehumidity_2m"][0]
                return ret
            this.log_error("location_details_ip", str(resp) + resp.content)
            return None
        except Exception as e:
            this.log_error("weather_details", e)
            return None

    def log_error(this, method, error):
        with open("error.log", "a") as f:
                f.writelines(f"{datetime.utcnow()} {method} {error} \n")