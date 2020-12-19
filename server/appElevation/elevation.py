#Have to pip install haversine, googlemaps, overpy
import googlemaps as gm
import haversine as hs
import overpy
import math
    
from array import *
    
gmaps = gm.Client(key="AIzaSyAs7JlLi3pn-VYlltsDfVwWS9J8AhbeM3U") #Key for API
def getAllPossibleWays(minLat = 39.905688, minLon = -75.349770, maxLat = 39.908144, maxLon = -75.346066):
    api = overpy.Overpass()
    result = api.query(f"""
        way({str(minLat)}, {str(minLon)}, {str(maxLat)}, {str(maxLon)});
        (._;>;);
        out body;
        """)
    waysList = []
    for i, way in enumerate(result.ways):
        lst = []
        for node in way.nodes:
            lst.append([node.lat, node.lon])
        waysList.append(lst)
    return waysList

def distanceBetweenTwoPoints(a, b):
    firstTuple = (a[0], a[1])
    secondTuple = (b[0], b[1])
    distance = hs.haversine(firstTuple, secondTuple)
    return (distance*1000)

def searchForNodes (personLat, personLong):
    searchThresholdLB = 75 #Lower Bound
    searchThresholdUB = 125 #Upper Bound
    overpassCallSearchRadius = 150 #Search Radius
    elevationThreshold = 0.01 #1m of elevation for 10m of distance
    
    goodRoutes = [[]] # holds the good routes with elevation data. Each column has lat1, long1, elevation1, lat2, long2, elevation2, total distance, total change in elevation

    #API Calls to OverPass for Nodes. Need to store lat and long
    nodes  = getAllPossibleWays() #When Parsing in, use the overpassCallSearchRadius
    #nodes[0][0].insert(0, 10) #importation into this array
    
    #API Calls to Roads API to snap nodes back onto road and then get elevation
    for node in nodes:
        for c in node:
            latLong = (c[0], c[1])
            result = gmaps.nearest_roads(latLong)
            if len(result) != 0:
                lat = result[0]["location"]["latitude"]
                lon = result[0]["location"]["longitude"]
                c[0] = lat
                c[1] = lon
                latLong = (c[0], c[1])
                c.append(gmaps.elevation(latLong)[0]["elevation"])
    
    for node in nodes:
        for firstComparison in node:
            for secondComparison in node:
                if len(firstComparison) == 3 and len(secondComparison) == 3:
                    dis = distanceBetweenTwoPoints(firstComparison, secondComparison)
                    if dis <= searchThresholdUB and dis >= searchThresholdLB:
                        elevation = firstComparison[2] - secondComparison[2]
                        first = firstComparison
                        second = secondComparison
                        if elevation < 0:
                            elevation = elevation * -1
                            third = second
                            second = first
                            first = third
                        if elevation/dis > elevationThreshold:
                            goodRoutes.append([first[0], first[1], first[2], second[0], second[1], second[2], dis, elevation])
    return goodRoutes

print(len(searchForNodes(1,1)))
