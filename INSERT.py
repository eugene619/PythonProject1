import sqlite3

conn = sqlite3.connect("example.db")
print("Successfully connected")

conn.execute("INSERT INTO Employee1 VALUES(1, 'Mark','Mugo', 45, 120000.00,'Manager')")
conn.execute("INSERT INTO Employee1 VALUES(2, 'Luke','Chojo', 25, 96000.00,'Admin')")
conn.execute("INSERT INTO Employee1 VALUES(3, 'Susanna','Abdi', 28, 210000.00,'HR')")
conn.execute("INSERT INTO Employee1 VALUES(4, 'Olsen','Sule', 46, 108000.00,'Supervisor')")
conn.execute("INSERT INTO Employee1 VALUES(5, 'Pierre','Didi', 41, 560000.00,'CEO')")

conn.commit()
print("Successfully inserted values into Employee Table")
