import googlemaps as gm
    
from array import *
    
gmaps = gm.Client(key="AIzaSyAs7JlLi3pn-VYlltsDfVwWS9J8AhbeM3U") #Key for API
    
def searchForNodes (personLat, personLong):
    searchThresholdLB = 75 #Lower Bound
    searchThresholdUP = 125 #Upper Bound
    overpassCallSearchRadius = 150 #Search Radius
    elevationThreshold = 0.1 #1m of elevation for 10m of distance
    
    #API Calls to OverPass for Nodes. Need to store lat and long
    nodes  = [[[]]]
    #nodes[0][0].insert(0, 10) #importation into this array
    
    #API Calls to Roads API to snap nodes back onto road and then get elevation
    for node in nodes:
        for c in node:
            latLong = (c[0], c[1])
            lat = gmaps.nearest_roads(latLong)[0]["location"]["latitude"]
            lon = gmaps.nearest_roads(latLong)[0]["location"]["longitude"]
            c[0] = lat
            c[1] = lon
            latLong = (c[0], c[1])
            c[2] = gmaps.elevation(latLong)[0]["elevation"]
    
    return lat
    
print(searchForNodes(2, 2))
