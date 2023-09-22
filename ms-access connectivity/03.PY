# INSERTING DATA INTO DATABASE...

import pyodbc

try:
    con_string = r"DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\Mohit Compuetrs\OneDrive\Documents\Database2.accdb"
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    myuser = (
        (6, 'data', 'data@gmail.com'),
        (7, 'shaka', 'shaka@gmail.com'),
        (8, 'dhaka', 'dhaka@gmail.com'),
    )
    cursor.executemany("INSERT INTO Table1 values(?,?,?)", myuser)
    conn.commit()
    print("Data Inserted")

except pyodbc.Error as e:
    print("Error in connection", e)

