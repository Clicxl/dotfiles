import requests
import json

api = "https://api.quotable.io/random/maxLength=15"


temperature = json.loads(data)["main"]["temp"]

print(f"{int(temperature)}°F")