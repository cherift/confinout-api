from flask import Flask, request

from models import DBModel, EventModel
from geopy.geocoders import Nominatim

app = Flask(__name__)
database = DBModel()

@app.route("/")
def home():
    return "Is working..." 

@app.route("/addevent", methods = ["GET", "POST"])
def addevent():

    params = request.args or request.form

    try:
        geolocator = Nominatim(user_agent="confinapp-api")
        location = geolocator.geocode(params["address"])

        try:
            longitude = location.longitude
            latitude = location.latitude
        except:
            return "{} is not valid adress.".format(params["address"])
        
        event = EventModel(params["place"], params["address"], params["price"],
                params[ "date"], params["description"], params["typeid"],
                params["link"] if not "link" in params else "NULL",
                params["number"] if not "number" in params else "NULL",
                longitude, latitude,
                params["inside"] if not "inside" in params else 1,
                params["available"] if not "available" in params else 1,
                params["handicap"] if not "handicap" in params else 1)

        event.save()
        
        return "New event saved."
    except:
        return "Error: ne or more required parameters (place, address, price, date, description, typeid) were missing."

if __name__ == "__main__":
    app.run(debug=True)



