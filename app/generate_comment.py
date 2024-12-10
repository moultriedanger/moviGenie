import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('movieGenie.db')
cursor = conn.cursor()

# Create Comments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Comments (
    comment_id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    username TEXT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES Movies (movie_id),
    FOREIGN KEY (username) REFERENCES Users (username)
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()
