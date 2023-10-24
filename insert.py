import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'Jeff', 33, 'Carlifania', 45000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'Arnold', 25, 'Texas', 55000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'Mark', 24, 'Texas', 55000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(4, 'Chris', 27, 'Texas', 55000.00)");
conn.commit()
print("Records created successfully")
conn.close()
