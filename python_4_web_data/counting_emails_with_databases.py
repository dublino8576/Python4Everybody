import sqlite3


connection = sqlite3.connect("emaildb.sqlite")
cursor = connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS Counts''')
cursor.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
user_input = input("Enter file: ")
file = open(user_input)
for line in file:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    #REMEMBER: you want to know emails from same organisation that can be from different people but same domain after @ symbol
    org = email.split("@")[1]
    #make an if statement by seeing if a SELECT statement is truthy or falsy. If the select results to None then insert values with count of 1 (if the number of count is None)checks the value of an attribute
    cursor.execute('''SELECT count FROM Counts WHERE org = ?''', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cursor.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))
connection.commit()
#if you move the commit inside the loop it will update each email at a time and will be taking much longer to run
sqlstr = cursor.execute('''SELECT * FROM Counts ORDER BY count DESC LIMIT 10''')

for row in sqlstr:
    print(row[0], row[1])
#stop speaking with database once its done
cursor.close()