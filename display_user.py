import connection
import pandas as pd
from mysql.connector import Error


def user_display():
    """
    menampilkan daftar user
    
    Parameter:
        fetch daftar_user sql
        
    Returns:
        daftar_user in dataframe
    """
    print("""
    ====================================================================
    ____________________________Daftar User ____________________________
    ====================================================================
    """)
    mydb = connection.connect()
    mycursor = mydb.cursor()

    #fetch daftar_user
    try:
        mycursor.execute("DESCRIBE daftar_user")
        tabel_user = pd.DataFrame(mycursor.fetchall())
    except Error as err:
        print(f"Error: {err}")
    
    try:
        mycursor.execute("SELECT * FROM daftar_user")
        result = pd.DataFrame(mycursor.fetchall())
        result = result.rename(columns = tabel_user.iloc[:,0]) #change column name
        print(result)
        print("===========================================================")
        return pd.DataFrame(result)
    except Error as err:
        print(f"Error: {err}")
