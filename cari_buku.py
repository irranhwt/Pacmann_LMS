import connection
import pandas as pd
from mysql.connector import Error

def search_buku():
    """
    mencari buku berdasarkan keyword
    
    Parameter:
        keyword : input keyword (str)
        
    Returns:
        tabel buku dari daftar_buku
    
    """
    try:
        mydb = connection.connect()
        mycursor = mydb.cursor()
        
        keyword = input("Input Keyword Buku: ") 
        
        #fetch daftar buku
        mycursor.execute("DESCRIBE daftar_buku") 
        tabel_buku = pd.DataFrame(mycursor.fetchall())
        
        #fetch daftar buku berdasarkan keyword
        mycursor.execute("SELECT * FROM daftar_buku WHERE NAMA_BUKU LIKE '%" + keyword + "%' OR KATEGORI LIKE '%" + keyword + "%'") 
        list_buku_keyword = mycursor.fetchall()
        
        #return result keyword
        if len(list_buku_keyword) < 1:
            print("Keyword Tidak Ditemukan")
        else:
            result = pd.DataFrame (list_buku_keyword)
            result = result.rename(columns = tabel_buku.iloc[:,0]) #change judul kolom
            print(result)
    
    except Error as err:
        print(f"Error: {err}")
