import os
import sqlite3
import json

#find path and connect
current_directory = os.path.dirname(__file__)
db_path = os.path.join(current_directory, 'movieGenie.db')
conn = sqlite3.connect(db_path)


# conn = sqlite3.connect(os.path.join(os.getcwd(), 'movieGenie.db'))
cursor = conn.cursor()

query = "INSERT INTO all_movies (movie_id, title, overview, poster, vote) VALUES (?, ?, ?, ?, ?)"
data =  []

# Path to the JSON file
file_path = '/Users/moultriedangerfield/Documents/Websites/moviGenie/www/data.json'

# Read and parse the JSON file
with open(file_path, 'r') as file:
    movies = json.load(file)

for i in range(0, len(movies)-1):

    id = movies[i]['id']
    title = movies[i]['title']
    description = movies[i]['overview']
    poster = movies[i]["poster_path"]
    vote = movies[i]['vote_average']
    
    d = (id, title, description, poster, vote)

    data.append(d)

cursor.executemany(query, data)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()