import requests
import pandas as pd
import json

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNjJkNzBkYTg0MWQyMWQ1ZDc1ZGQ3NGUyYjlkNmNiZiIsIm5iZiI6MTcyNjM2ODUxMy4xNDQyOTcsInN1YiI6IjY2ZDIwZWRhYjI3MGJjYjlmY2E3ZjE4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zSNI8OLZGu0iuD0IWm0Qpv-eTHQQniytv6LLmG97QJU"
}

response = requests.get(url, headers=headers)

#Gather json objects
movies = response.json()

results = movies['results']

base_url = "https://image.tmdb.org/t/p/"

image_size = "w1280"

for result in results:
    image_path = result["poster_path"]

    full_path = f'{base_url}{image_size}{image_path}'

    result["poster_path"] = full_path

json_object = json.dumps(results, indent=4)

with open("www/data.json", "w") as outfile:
    outfile.write(json_object)