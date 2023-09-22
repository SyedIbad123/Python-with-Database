# DELETING DATA...

import pyodbc

try:
    con_string = r"DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\Mohit Compuetrs\OneDrive\Documents\Database2.accdb"
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    user_id = 3
    cursor.execute("DELETE FROM Table1 Where id = ?",(user_id))
    conn.commit()
    print("Data deleted")

except pyodbc.Error as e:
    print("Error in connection", e)

    
