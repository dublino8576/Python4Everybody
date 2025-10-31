#EXPLORE MANY TO MANY RELATIONSHIP WITH MYSQLite

'''
This application will read roster data in JSON format, parse the file, and then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file:


Dowload your roster.json data
And save it as roster_data.json. Move the downloaded file into the same folder as your roster.py program.
'''

import sqlite3, json

connection = sqlite3.connect("rosterdb.sqlite")
cursor = connection.cursor()
cursor.executescript('''
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS User
''')
cursor.executescript('''
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE);
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE);
    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id, course_id))
    ''')
    #FOR MEMBER TABLE WE CREATE A COMPOSITE PRIMARY KEY WHICH IS COMBO BETWEEN THE 2 FOREIGN KEYS

file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "roster_data.json"
try:
    file = open(file_name)
except:
    print("sorry file not found", file_name)

parsed_file = json.load(file)
#turn json into a list as it is a string otherwise
for line in parsed_file:
    person_name = line[0]
    course_name = line[1]
    person_role = line[2]
    
    cursor.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (person_name,))
    cursor.execute('SELECT id FROM User WHERE name=?', (person_name,))
    user_id = cursor.fetchone()[0]
    
    cursor.execute('INSERT OR IGNORE INTO Course (name) VALUES (?)', (course_name,))
    cursor.execute('SELECT id FROM Course WHERE name=?', (course_name,))
    course_id = cursor.fetchone()[0]
    #print(course_id, user_id) will print all the course_id and user_id found, the ones there are inserted and the ones that are ignored, since the insert or ignore statement are run each time
    cursor.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, person_role))
connection.commit()

cursor.execute('''
    SELECT User.name,Course.name, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.name DESC, Member.role DESC LIMIT 2;        
''')
result = cursor.fetchall()
print(result)
cursor.execute('''SELECT 'XYZZY' || hex(User.name || Course.name || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;''')
#GENERATE CODE FOR EACH STUDENT: do a select statement with a valid code starting with XYZZY and concatenate the string to the hexodecimal number of user.name, course.name, member.role concatenated as well
final_result = cursor.fetchall()
print(final_result)
connection.close()