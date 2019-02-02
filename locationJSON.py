import json
import folium
import colorsys
from math import log

def toTwoDigitHex(num):
    hexValue = hex(int(num * 255))[2:]

    if (len(hexValue) < 2):
        hexValue = hexValue.zfill(2)
    
    return hexValue

print("Loading json...")

jsonFile = open("Location History.json")
locationHistory = json.load(jsonFile)

locations = []
counts = []

print("Populating lists...")

for location in locationHistory['locations']:
    coordinate = (round(location['latitudeE7'] / (10 ** 7), 2), round(location['longitudeE7'] / (10 ** 7), 2))
    
    if coordinate in locations:
        counts[(locations.index(coordinate))] += 1
    else:
        locations.append(coordinate)
        counts.append(1)

m = folium.Map(prefer_canvas = True)

print("Adding markers...")

for num in range(len(locations)):
    color = colorsys.hsv_to_rgb(0.65 - ((log(counts[num], 2) + 1) / (log(max(counts), 2) + 1) / 1.54), 1.0, 1.0)
    folium.Circle(locations[num], radius = 500, fill = True, fill_opacity = 0.4, color = f"#{toTwoDigitHex(color[0])}{toTwoDigitHex(color[1])}{toTwoDigitHex(color[2])}").add_to(m)

print("Saving...")

m.save("location_history.html")

print("Done")