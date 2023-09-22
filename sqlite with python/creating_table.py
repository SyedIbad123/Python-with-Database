# SQLITE IS CASE SENSTITVE...

import sqlite3

conn = sqlite3.connect('customer.db')

# creating a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email_address text
    )""") # WE USE TRIPLE DOC STRING WHEN WIRITNG CODE IN DIFFERENT LINES..
conn.commit()
conn.close()




# c.execute(''' CREATE TABLE customers first_name DATATYPE,last_name DATATYPE email_address DATATYPE)''') # WE USE SINGLE DOC STRING WHEN WIRITNG CODE IN SINGLE LINE.


