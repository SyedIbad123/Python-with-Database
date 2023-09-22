# FETCHING AND SELECTING DATA...

import pyodbc

try:
    con_string = r"DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\Mohit Compuetrs\OneDrive\Documents\Database2.accdb"
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()
    cursor.execute("SELECT * from Table1")

    for row in cursor.fetchall():
        print(row)




except pyodbc.Error as e:
    print("Error Connection in database", e)