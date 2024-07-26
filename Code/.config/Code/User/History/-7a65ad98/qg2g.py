import urllib.request
import json

LAT = "12.97160° N"
LON = "LONGITUDE GOES HERE"
KEY = "KEY GOES HERE"

data = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat="+LAT+"&lon="+LON+"&appid="+KEY+"&units=imperial").read()

temperature = json.loads(data)["main"]["temp"]

print(f"{int(temperature)}°F")