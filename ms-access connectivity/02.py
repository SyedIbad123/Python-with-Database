# CONNECTING TO DATABASE OF MS-ACCESS

import pyodbc

try:
    con_string = r"DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\Mohit Compuetrs\OneDrive\Documents\Database2.accdb"
    conn = pyodbc.connect(con_string)
    print("Database is connected")

except pyodbc.Error as e:
    print("Error in connecting database",e)



