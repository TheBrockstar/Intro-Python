# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 42,
        "long": 42,
        "name":"The Truth"
    },
    {
        "lat": 777,
        "long": 777,
        "name": "Heaven"
    },
    {
        "lat": 666,
        "long": 666,
        "name": "Hell" 
    }

]

# Write a loop that prints out all the field values for all the waypoints

for w in waypoints:
    print("latitude: ", w["lat"], "longitude: ", w["long"], "name: ", w["name"])

print("")

# Add a new waypoint to the list
newWaypoint = {
    "lat": 3,
    "long": 3,
    "name":"The Triangle"
}

waypoints.append(newWaypoint)

for w in waypoints:
    print("latitude: ", w["lat"], "longitude: ", w["long"], "name: ", w["name"])