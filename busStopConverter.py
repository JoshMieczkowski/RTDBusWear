import os
import json
path =  os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/"

fileName = "bus_stops.txt"

jsonData = []

with open(path + fileName) as file:
    for line in file:
        data = line.split(",")
        
        stopID = data[0];
        stopCode = data[1];
        stopName = data[2];
        stopDesc = data[3];
        latitude = data[4];
        longitude = data[5];
        
        newData = {
        	'stopID' : stopID,
        	'stopCode' : stopCode,
        	'stopName' : stopName,
        	'stopDesc' : stopDesc,
        	'latitude' : latitude,
        	'longitude' : longitude,
        }
        
        jsonData.append(newData)
        
with open(path + 'busStopData.json', 'w') as outfile:  
    json.dump(jsonData, outfile)
        