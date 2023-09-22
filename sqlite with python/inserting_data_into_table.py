import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

many_customer = [
    ('wes', 'brown', 'wes@gmail.com'),
    ('mahad', 'black', 'mahad123@gmail.com'),
    ('ahad', 'green', 'ahad@gmail.com')
]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customer)

print("Command executes successfully...")
conn.commit()
conn.close()
