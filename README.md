# ConfinOUT API

This project manages the CRUD part of the ConfinOUT android mobile app.

It's an API created in Python by using the Flask library.

## Install

`git clone https://github.com/cherift/confinout-api.git`

## Set up the app

Sets in the variables evironnement these parameters :  

`$CUSER` the database user name

`$CPWD` the database password
 
`CHOST` the database url

`CDBNAME` the database name

## Use Cases

### - Add a new event

`POST /addevent`

|Paraemter | type | Description|
|----------|------|------------|
|place|string|the name of the place|
|address|string|the place full adress|
|price|float|the event price|
|date|datetime|the date and the hour|
|description|string|the event description|
|typeid|integer|the event type|

#### Response

`
    message : string
`

### - Get the list of events

`GET /events`

#### Response


    {
        count : integer
        "result" : [{
            "id"          : integer
            "place"       : string
            "address"     : string
            "price"       : string
            "date"        : datetime
            "description" : string
            "typeid"      : integer
            "link"        : string
            "number"      : integer
            "longitude"   : float
            "latitude"    : float
            "inside"      : boolean
            "available"   : boolean
            "handicap"    : boolean
        }]
    }



### - Cancel an event

`POST /cancel/event_id`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|

#### Response

`
    message : string
`

### - Add a new event type

`POST /addtype/name`

|Paraemter | type | Description |
|----------|------|------------|
|name|string|the name of the event type|

#### Response

`
    message : string
`

### - Get all event types

`GET /types`

#### Response


    {
        "result" : [{
            "id" : integer 
            "name" : string
        }]
    }   

### - Rate an event

`POST /rate/event_id/value`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|
|value|intger|the rate value|

#### Response

`
    message : string
`

### - Gets the average rate of an event

`GET /rates/<event_id>`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|

#### Response

    {
        "event" : integer
        "rate"  : float
    }

### - Add a comment for an event

`POST /comment/event_id/message`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|
|message|string|the comment message|

#### Response

`
    message : string
`

### - Get list of comments for an event

`GET /comments/event_id`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|

#### Response

    {
        "count"  : integer,
        "result" : [{
            "date"    : datetime
            "message" : string
        }]
    }

### - Add notification message for an event

`POST /notify/event/message`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|
|message|string|the notifcaiton message|

#### Response

`
    message : string
`

### - Get the list of notification of an event

`GET /notifications/event_id`

|Paraemter | type | Description |
|----------|------|------------|
|event_id|integer|the id of the event|

#### Response

    {
        "count"  : integer,
        "result" : [{
            "date"    : datetime
            "message" : string
        }]
    }



## Maintainers

This project is maintened by :
- [Abdoulaye Chérif Touré](https://github.com/cherift)
- [Jean Claude Tarby](https://github.com/jctarby)
