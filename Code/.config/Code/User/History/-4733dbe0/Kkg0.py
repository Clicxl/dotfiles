import urllib.request
import json

LAT = "12.9716° N"
LON = "77.5946° E."
KEY = "KEY GOES HERE"

data = urllib.request.urlopen("https://api.quotable.io/random").read()

temperature = json.loads(data)["main"]["temp"]

print(f"{int(temperature)}°F")