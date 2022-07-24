import connection
import pandas as pd
from mysql.connector import Error


def pinjam_display():
    """
    menampilkan daftar/riwayat peminjaman
    
    Parameter:
        fetch daftar_pinjam sql
        
    Returns:
        daftar_pinjam in dataframe
    """ 
    
    print("""
    ______________________Daftar/Riwayat Peminjaman ____________________
    ====================================================================
    """)
    mydb = connection.connect()
    mycursor = mydb.cursor()

    try:
        mycursor.execute("DESCRIBE daftar_pinjam")
        tabel_pinjam = pd.DataFrame(mycursor.fetchall())
    except Error as err:
        print(f"Error: {err}")
    
    try:
        mycursor.execute("SELECT * FROM daftar_pinjam")
        result = pd.DataFrame(mycursor.fetchall())
        result = result.rename(columns = tabel_pinjam.iloc[:, 0]) #change column name
        print(result)
        print("==========================================")
        return pd.DataFrame(result)
    except Error as err:
        print(f"Error: {err}")
