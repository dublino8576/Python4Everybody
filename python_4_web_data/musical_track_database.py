import sqlite3
connection = sqlite3.connect("trackdb.sqlite")
cursor = connection.cursor()
cursor.executescript('''
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Artist
''')
cursor.executescript('''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

file = open("tracks.csv")
for line in file:
    
    new_line = line.strip()
    song_info= new_line.split(",")
    if len(song_info) < 6:
        continue
    track = song_info[0]
    artist = song_info[1]
    album = song_info[2]
    count = song_info[3]
    rating = song_info[4]
    length = song_info[5]
    genre = song_info[6] 
    cursor.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
    cursor.execute('''SELECT id FROM Artist WHERE name=?''', (artist,))
    #WE HAVENT CREATED ANY FOREIGN KEY IN THE SCHEMA SO WE ARE MANUALLY ADDING THE ARTICLE ID, GENRE ID, ALBUM ID IN THE TRACKS TABLE OR OTHER TABLES THAT ARE CHILD TABLES.
    artist_id = cursor.fetchone()[0]
    #THIS RETAINS THE ARTICLE ID WHICH CAN BE USED TO BE INJECTED IN A CHILD TABLE (THIS IS AN OBJECT CONTAINING THE ONE ELEMENT TUPLE OF ID)
    cursor.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
    cursor.execute('''SELECT id FROM Genre WHERE name=?''', (genre,))
    genre_id = cursor.fetchone()[0]
    cursor.execute('''INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)''', (artist_id, album))
    cursor.execute('''SELECT id FROM Album WHERE title=?''', (album,))
    album_id = cursor.fetchone()[0]
    cursor.execute('''INSERT OR REPLACE INTO Track (
                   title,
                   album_id,
                   genre_id,
                   len, rating, count
                   )
                   VALUES (?, ?, ?, ?, ?, ?)''', (track, album_id, genre_id, length, rating, count))
cursor.execute('''SELECT Track.title, Artist.name, Album.title,     Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID 
    AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
#commit allows you to SAVE the data onto the database so that you can see it on the sqlite file with db browser program
connection.commit()
row = cursor.fetchall()
print(row)
#there is no joining performed here but this join is used to grade the assignment
#selects which attributes you want to see in the table and track table joins all the tables. the on clause makes sure that only matches with that ID are seen one and there arent any doubles in different combination order.
cursor.close()
