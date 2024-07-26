import requests
import json

api = "https://api.quotable.io/random/maxLength=15"

quote = requests.get(api).json()
print(quote)

# temperature = json.loads(data)["main"]["temp"]

# print(f"{int(temperature)}°F")