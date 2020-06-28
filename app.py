from flask import Flask, request

from models import DBModel, EventModel, TypeModel, NoteModel, CommentModel
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
        "count" : len(database.events()),
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


@app.route("/cancel/<int:event_id>")
def cancel(event_id):
    """
    Cancels an event

    Parameters
    ----------
    event_id : the id of the event to cancel
    """
    return database.cancel(event_id)


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


@app.route("/rate/<int:event_id>/<int:value>")
def rate(event_id, value):
    """
    Marks an event

    Paramters
    ---------
    event_id: the id of the event to mark
    value: the rate gived to the event
    """
    try:    
        assert 1 <= value and value <= 5

        note = NoteModel(event_id, value)
        try:
            note.save()
            return "Your note is saved."
        except:
            return "No event with the id {} founded".format(event_id)
    except AssertionError:
        return "rate value must be between 1 and 5"


@app.route("/rates/<int:event_id>")
def rates(event_id):
    """
    Gets and an event rates.

    Paramters
    ---------
    event_id: the id of the event
    """
    result = database.rates(event_id)
    return json.dumps({
        "event" : event_id,
        "rate"  : round(float(result), 1) if result else 0
    })


@app.route("/comment/<int:event_id>/<message>")
def comment(event_id, message):
    """
    Comments an event

    Paramters
    ---------
    event_id: the id of the event to comment
    message: the comment gived to the event
    """
    com = CommentModel(event_id, message)

    try:
        com.save()
        return "Your comment is saved."
    except:
        return "No event with the id {} founded".format(event_id)    


@app.route("/comments/<int:event_id>")
def comments(event_id):
    """
    Gets an event comments.

    Paramters
    ---------
    event_id: the id of the event
    """
    result = database.comments(event_id)

    return json.dumps({
        "count"  : len(result),
        "result" : [{
                "date"    : c[0].strftime("%d/%m/%Y"),
                "message" : c[1]
            } for c in result
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)



