import os
import json
path =  os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/"

fileName = "bus_stop_times.txt"

jsonData = []

with open(path + fileName) as file:
    for line in file:
        data = line.split(",")
        
        tripID = data[0];
        arrivalTime = data[1];
        departureTime = data[2];
        stopID = data[3];
        stopSequence = data[4];
        
        newData = {
        	'tripID' : tripID,
        	'arrivalTime' : arrivalTime,
        	'departureTime' : departureTime,
        	'stopID' : stopID,
        	'stopSequence' : stopSequence
        }
        
        jsonData.append(newData)
        
with open(path + 'busTimeData.json', 'w') as outfile:  
    json.dump(jsonData, outfile)
        