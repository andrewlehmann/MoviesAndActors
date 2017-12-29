import json, requests

def reviewScore(movie_name):
  url = "http://www.omdbapi.com/?apikey=84585783&"
  parameters = {
    "type": "Movie",
    "t": movie_name
  }
  response = requests.get(url=url, params=parameters)
  data = json.loads(response.text)
  review = data['imdbRating']
  return review
  
print(reviewScore("Die Hard"))