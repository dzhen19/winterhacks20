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
    
    #API Calls to Roads API to snap nodes back onto road
    thisTuple = (40.714728, -73.998672)
    #results = gmaps.nearest_roads(thisTuple)
    results = gmaps.elevation(thisTuple)

    #for node in nodes:
        #Call API elevation for each node and store as 3rd (index 2) in node table
    #    for c in node:
    #        latLong = (c[0], c[1])
    #        gmaps.elevation(latLong)
    
    return results
    
print(searchForNodes(2, 2))
