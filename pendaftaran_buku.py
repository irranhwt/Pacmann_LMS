import connection
from mysql.connector import Error
import datetime
import sys

def daftar_buku():
    """
    melakukan insert data buku ke database daftar_buku
    
    Parameter:
        id_buku = input nama user (str)
        tgl_lahir = input tgl_lahir (date)
        pekerjaan = input pekerjaan (str)
        alamat = input alamat (str)
        
    Returns:
        database daftar_buku updated
        
    """   
    mydb = connection.connect()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT ID_BUKU FROM daftar_buku")     #fetch id_buku  
        list_buku = mycursor.fetchall()
        list_id_buku = []
        for i in list_buku:
            list_id_buku.append(str(i[0]))
        
        check_buku = False #check id buku baru for duplicate id
        while check_buku == False:
            id_buku = input("Masukkan Kode Buku Baru Yang Akan Didaftarkan: ") 
            if id_buku in list_id_buku:
                print(f"id_buku {id_buku} sudah terdaftar, masukkan format ID lainnya")
                check_buku = False
            else:
                check_buku = True
        
    except Error as err:
        print(f"Error: {err}")
      
    nama_buku = input("Masukkan Nama Buku: ")
    kategori = input("Masukkan Kategori Buku: ")
    stock = input("Masukkan Stock Buku: ")
    data = (id_buku, nama_buku, kategori, stock)
    
    try:
        query = """INSERT INTO daftar_buku(ID_BUKU,NAMA_BUKU,KATEGORI,STOCK) VALUES(%s,%s,%s,%s)"""
        mydb = connection.connect()
        mycursor = mydb.cursor()
        mycursor.execute(query, data)
        mydb.commit()
        print("""
        Query berhasil dieksekusi
        ==========================
        Data Entered Successfully
        """)
    except Error as err:
        print(f"Error: {err}")