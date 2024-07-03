import sqlite3

conn = sqlite3.connect("example.db")
print("Successfully connected")

conn.execute("DELETE FROM Employee1 WHERE ID = 2")
conn.commit()

data = conn.execute("SELECT * FROM Employee1")

for Employee1 in data:
    print("ID:", Employee1[0])
    print("FIRSTNAME:", Employee1[1])
    print("LASTNAME:", Employee1[2])
    print("AGE:", Employee1[3])
    print("SALARY:", Employee1[4])
    print("POSITION:", Employee1[5])