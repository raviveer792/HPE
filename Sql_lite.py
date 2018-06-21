import _sqlite3
conn = _sqlite3.connect("Student.db")

cursor=conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")
'''cursor.execute("""CREATE TABLE users(
id NOT NULL PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL 
)""")'''

cursor.execute('INSERT INTO users VALUES(1,'
               '"Hello","546446")')
#cursor.execute('INSERT INTO cars VALUES(NULL,"Fiat","Polo",1)')
#cursor.execute('INSERT INTO cars VALUES(NULL,"BMW","Polo",1)')