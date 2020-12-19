import googlemaps as gm
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
    lat1 = (a[0]/180) * math.pi
    lat2 = (b[0]/180) * math.pi
    lon1 = (a[1]/180) * math.pi
    lon2 = (b[1]/180) * math.pi
    R = 6371
    x = (lat2 - lat1) * math.cos((lon1+lon2)/2)
    # print(math.cos((lon1+lon2)/2))
    y = (lon2 - lon1)
    distance = R * math.sqrt((x*x)+(y*y))
    return distance

def searchForNodes (personLat, personLong):
    searchThresholdLB = 75 #Lower Bound
    searchThresholdUB = 125 #Upper Bound
    overpassCallSearchRadius = 150 #Search Radius
    elevationThreshold = 0.1 #1m of elevation for 10m of distance
    
    goodRoutes = [[]] # holds the good routes with elevation data. Each column has lat1, long1, elevation1, lat2, long2, elevation2, total distance, total change in elevation

    #API Calls to OverPass for Nodes. Need to store lat and long
    nodes  = getAllPossibleWays() #When Parsing in, use the overpassCallSearchRadius
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
    
    for node in nodes:
        for firstComparison in node:
            for secondComparison in node:
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
                        #Perform API Call on google routes to see if Dis is approximately the same
                        #If it is approx the same, add to good routes table
                        pass
    return goodRoutes


thisTuple1 = (39.902941, -75.347832)
thisTuple2 = (39.903344, -75.346205)
print(distanceBetweenTwoPoints(thisTuple1, thisTuple2))


