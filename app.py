from flask import Flask, request

from models import DBModel, EventModel, TypeModel
from geopy.geocoders import Nominatim
import json

app = Flask(__name__)
database = DBModel()

@app.route("/")
def home():
    return "Is working..." 

@app.route("/addevent", methods = ["GET", "POST"])
def addevent():
    """
    Adds a new event
    """

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
                longitude, latitude,
                params["link"] if "link" in params else "NULL",
                params["number"] if "number" in params else "NULL",
                params["inside"] if "inside" in params else 1,
                params["available"] if "available" in params else 1,
                params["handicap"] if "handicap" in params else 1)
        
        event.save()
        
        return "New event saved."
    except:
        return "Error: one or more required parameters (place, address, price, date, description, typeid) were missing."


@app.route("/events")
def events():
    """
    Gets all events
    """
    return json.dumps({
        "result" : [{
            "id"          : e[0],
            "place"       : e[1],
            "address"     : e[2],
            "price"       : e[3],
            "date"        : e[4].strftime("%d/%m/%Y, %H:%M:%S"),
            "description" : e[5],
            "typeid"      : e[6],
            "link"        : e[7],
            "number"      : e[8],
            "longitude"   : e[9],
            "latitude"    : e[10],
            "inside"      : e[11],
            "available"   : e[12],
            "handicap"    : e[13]
        } for e in database.events()]
    }, ensure_ascii=False).encode('utf8')

@app.route("/addtype/<name>")
def addtype(name):
    """
    Adds new event type

    Parameters
    ----------
    name: the name of the event type
    """
    type = TypeModel(name)
    type.save()
    return "new type of event added"

@app.route("/types")
def types():
    """
    Gests all event types 
    """
    return json.dumps({
        "result" : [{
            "id" : t[0], 
            "name" : t[1] 
        } for t in  database.types()]
    }, ensure_ascii=False).encode('utf8')

if __name__ == "__main__":
    app.run(debug=True)



