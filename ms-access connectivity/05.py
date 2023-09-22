# UPDATE DATA...

import pyodbc

try:
    con_string = r'Driver=Microsoft Access Driver (*.mdb, *.accdb);DBQ=C:\Users\Mohit Compuetrs\OneDrive\Documents\Database2.accdb'
    conn = pyodbc.connect(con_string)
    
    new_name = "updateddata"
    user_id = 4
    cursor = conn.cursor()
    curr = cursor.execute("UPDATE Table1 SET name = ? Where id = ? ",(new_name,user_id)) 
    conn.commit()
    print("Data inserted")
 
except pyodbc.Error as e:
    print("Error in connection",e)