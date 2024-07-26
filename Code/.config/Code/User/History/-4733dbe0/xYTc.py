import urllib.request
import json

data = urllib.request.urlopen("https://api.quotable.io").read()

temperature = json.loads(data)["main"]["temp"]

print(f"{int(temperature)}°F")