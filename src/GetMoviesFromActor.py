import json, requests


def create_search_person_url(actor_name):
    return "https://api.themoviedb.org/3/search/person?api_key=838ea5778063d73706349419667983dc&language=en-US&query=" + actor_name + "&page=1&include_adult=false"

def create_get_movies_by_actor_url(actor_id):
    return "https://api.themoviedb.org/3/discover/movie?api_key=838ea5778063d73706349419667983dc&language=en-US&sort_by=primary_release_date.asc&include_adult=false&include_video=false&with_people=" + str(actor_id)


def call_api(url):
    response = requests.get(url=url)
    data = json.loads(response.text)
    return data


def get_actor_id(actor_name):
    search_results = call_api(create_search_person_url(actor_name))
    actor_id = search_results['results'][0]['id']
    return actor_id

def get_movies_by_actor(actor_name):
    actor_id = get_actor_id(actor_name)
    url = create_get_movies_by_actor_url(actor_id)
    data = call_api(url)
    return [{
        'release_date': movie['release_date'], 
        'title': movie['original_title'] } for movie in data['results']]
    


print(get_movies_by_actor("Tom Cruise"))