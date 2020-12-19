import overpy
from server.appElevation.elevation import *

def main():
    minLat, minLon, maxLat, maxLon =  (boundingBox((37.773972, -122.431297), 150))
    api = overpy.Overpass()
    result = api.query(f"""
        way({minLat[0]}, {minLon[1]}, {maxLat[0]}, {maxLon[1]});
        (._;>;);
        out body;
        """)
    waysList = []
    for i, way in enumerate(result.ways):
        lst = []
        for node in way.nodes:
            lst.append([node.lat, node.lon])
        waysList.append(lst)
    print(waysList[0])
main()
