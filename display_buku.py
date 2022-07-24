import connection
import pandas as pd
from mysql.connector import Error


def buku_display():
    """
    menampilkan daftar buku
    
    Parameter:
        fetch daftar_buku sql
        
    Returns:
        daftar_buku in dataframe
    """
    
    print("""
    ===========================================================
    ____________________Daftar Buku____________________________
    ===========================================================
    """)
    
    mydb = connection.connect()
    mycursor = mydb.cursor()

    #fetch daftar_buku
    try:
        mycursor.execute("DESCRIBE daftar_buku")
        tabel_buku = pd.DataFrame(mycursor.fetchall())
    except Error as err:
        print(f"Error: {err}")
    
    try:
        mycursor.execute("SELECT * FROM daftar_buku")
        result = pd.DataFrame(mycursor.fetchall())
        result = result.rename(columns = tabel_buku.iloc[:,0]) #change column name
        print(result)
        print("===========================================================")
        return pd.DataFrame(result)
    except Error as err:
        print(f"Error: {err}")
