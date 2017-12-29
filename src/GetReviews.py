import json, requests

url = "http://www.omdbapi.com/?apikey=84585783&"

parameters = {
    "type": "Movie",
    "t": "Die Hard"
}

response = requests.get(url=url, params=parameters)
data = json.loads(response.text)
