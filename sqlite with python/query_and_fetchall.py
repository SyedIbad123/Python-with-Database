import sqlite3

conn = sqlite3.connect('customer.db')
c = conn.cursor()

c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchmany())


items = c.fetchall()

for item in items:
    print(item[0] + " " + item[1] + " " + item[2]) 


conn.commit()
conn.close()
