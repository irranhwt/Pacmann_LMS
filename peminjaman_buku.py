import connection
import pandas as pd
from mysql.connector import Error
from datetime import date


def pinjam_buku():
    """
    melakukan pengecekan user & pengecekan buku serta update daftar_pinjam dan stock pada daftar_buku
    
    Parameter:
        id_user_pinjam : input id_user (int)
        id_buku_pinjam : input id_buku (str)
        
    Returns:
        database daftar_pinjam updated
        database daftar_buku updated
        
    """
    
    mydb = connection.connect()
    mycursor = mydb.cursor()
    today = date.today() 

    try:
        mycursor.execute("SELECT ID_USER FROM daftar_user") #fetch id user
        list_id_user = mycursor.fetchall()
        id_user = []
        for i in list_id_user:
            id_user.append(str(i[0]))
               
        id_user_pinjam = input("Input ID User Yang Akan Meminjam Buku: ") #check id user peminjam 
        if id_user_pinjam in id_user:
            print(f"id_user: {id_user_pinjam}")
        else:
            print("ID User Tidak Ditemukan!")
            id_user_pinjam = input("Input ID User Yang Akan Meminjam Buku: ")
        
    except Error as err:
        print(f"Error: {err}")
   
    #cari nama user sesuai Id User Peminjam dan print
    try:
        mycursor.execute("SELECT U_NAME FROM daftar_user WHERE ID_USER =" + id_user_pinjam)  
        nama_user = mycursor.fetchall()[0][0]
        print(f"Nama Peminjam: {nama_user}")
    except Error as err:
        print(f"Error: {err}")   
  
    try:
        mycursor.execute("SELECT ID_BUKU FROM daftar_buku")     #fetch id_buku  
        daftar_id_buku = mycursor.fetchall()
        list_buku = []
        for i in daftar_id_buku:
            list_buku.append(str(i[0]))
        
        id_buku_pinjam = input("Masukkan Kode Buku Yang Akan Dipinjam: ") #check kode buku yang akan dipinjam
        if id_buku_pinjam in list_buku:
            print(f"id_buku: {id_buku_pinjam}")
        else:
            print("Kode Buku Tidak Ditemukan")
            id_buku_pinjam = input("Masukkan Kode Buku Yang Akan Dipinjam:  ")  
        
    except Error as err:
        print(f"Error: {err}")
    
    #cari nama buku sesuai ID Buku yang dipinjam dan print
    try:
        mycursor.execute("SELECT NAMA_BUKU FROM daftar_buku WHERE ID_BUKU =" + id_buku_pinjam) 
        nama_buku = mycursor.fetchall()[0][0]
        print(f"Judul Buku: {nama_buku}")
    except Error as err:
        print(f"Error: {err}")
    
    #update stock pada daftar_buku 
    #update field pada daftar_pinjam
    try:
        mycursor.execute("SELECT STOCK FROM daftar_buku WHERE ID_BUKU =" + id_buku_pinjam) #cek stock buku sesuai ID Buku
        stock_buku = mycursor.fetchall()
        sisa_stock = stock_buku[0][0]
        print(f"Stock Buku Tersedia: {sisa_stock}")
        if sisa_stock == 0:
            print("Stock Buku Habis")
        else:
            print(f"Buku Dipinjamkan ke: {nama_user}")
            sisa_stock -= 1
            print(f"Stock Buku Saat Ini: {sisa_stock}")
            mycursor.execute(f"UPDATE daftar_buku SET STOCK = {sisa_stock} WHERE ID_BUKU = {id_buku_pinjam}")
            mycursor.execute("INSERT INTO daftar_pinjam(ID_USER, NAMA_USER, ID_BUKU, NAMA_BUKU, TANGGAL_PINJAM)\
                              VALUES(%s,%s,%s,%s,%s)",(id_user_pinjam, nama_user, id_buku_pinjam, nama_buku, today))           
            mydb.commit()
            print("""
            Query berhasil dieksekusi
            ==========================
            Data Entered Successfully
            """)
    except Error as err:
        print(f"Error: {err}")

    
    
    