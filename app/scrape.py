import requests
import pandas as pd
import json

#Request the data
url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNjJkNzBkYTg0MWQyMWQ1ZDc1ZGQ3NGUyYjlkNmNiZiIsIm5iZiI6MTcyNjM2ODUxMy4xNDQyOTcsInN1YiI6IjY2ZDIwZWRhYjI3MGJjYjlmY2E3ZjE4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zSNI8OLZGu0iuD0IWm0Qpv-eTHQQniytv6LLmG97QJU"
}
print('helo')
# /8cdWjvZQUExUUTzyp4t6EDMubfO.jpg

response = requests.get(url, headers=headers)

#Gather json objects
movies = response.json()

# print(len(movies))

results = movies['results']

# Write to file
json_object = json.dumps(results, indent=4)


with open("data.json", "w") as outfile:
    outfile.write(json_object)
