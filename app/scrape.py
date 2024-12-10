import requests
import pandas as pd
import json

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNjJkNzBkYTg0MWQyMWQ1ZDc1ZGQ3NGUyYjlkNmNiZiIsIm5iZiI6MTcyNjM2ODUxMy4xNDQyOTcsInN1YiI6IjY2ZDIwZWRhYjI3MGJjYjlmY2E3ZjE4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zSNI8OLZGu0iuD0IWm0Qpv-eTHQQniytv6LLmG97QJU"
}

movie_list = []

for page in range(1, 3):
    url = f'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page}&sort_by=popularity.desc/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg'

    response = requests.get(url, headers=headers)

    movies = response.json()['results']

    movie_list.extend(movies)

#add prefix to poster. WILL NEED TO ADD BACKDROP TOO EVENTUALLY--Moultrie
for m in movie_list:
    m['poster_path'] = 'https://image.tmdb.org/t/p/w1280' + m['poster_path']

# print(movie_list[0]['poster_path'])

json_object = json.dumps(movie_list, indent=4)

with open("www/data.json", "w") as outfile:
    outfile.write(json_object)