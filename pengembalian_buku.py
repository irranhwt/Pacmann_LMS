import pandas as pd
from mysql.connector import Error
from datetime import date
import connection


def kembali():
    """
    melakukan pengecekan user peminjam dan update informasi pada daftar_pinjam serta update stock pada daftar_buku
    
    Parameter:
        id_peminjam : input id_user (int)
        id_buku_pinjam : input id_buku (str)
        
    Returns:
        database daftar_pinjam updated
        database daftar_buku updated
        
    """
    mydb = connection.connect()
    mycursor = mydb.cursor()
    today = date.today()
    
    try:
        #fetch id user dari daftar_pinjam
        mycursor.execute("SELECT ID_USER FROM daftar_pinjam WHERE TANGGAL_PENGEMBALIAN IS NULL") 
        id_user_pinjam = mycursor.fetchall()
        
        if len(id_user_pinjam)>0: #bila ada peminjaman
            id_user_kembali = input("Masukkan ID User Yang Akan Melakukan Pengembalian: ")
            list_id_pinjam = []
            
            for i in id_user_pinjam: #return list id user yang melakukan peminjaman
                list_id_pinjam.append(str(i[0]))
            
            if id_user_kembali in list_id_pinjam: #cek id user yang mengembalikan
                print(f"ID User Peminjam : {id_peminjam}")
            else:
                print("ID User Peminjam Tidak Ditemukan! Masukkan ID User Yang Sesuai")
                id_peminjam = input("Masukkan ID User Peminjam: ")
            
            mycursor.execute("SELECT ID_BUKU, NAMA_BUKU, TANGGAL_PINJAM FROM daftar_pinjam WHERE ID_USER="+ id_peminjam + "\
                              AND TANGGAL_PENGEMBALIAN IS NULL") #fetch informasi buku yang dipinjam
            list_pinjam = mycursor.fetchall()
            id_buku_pinjam = []
            print("Informasi Peminjaman:")
            info_pinjam = pd.DataFrame(list_pinjam)
            print(info_pinjam)
            for i in list_pinjam:
                id_buku_pinjam.append(str(i[0]))
           
            id_buku_kembali = input("Masukkan ID Buku Yang Ingin Dikembalikan: ")
            if id_buku_kembali not in id_buku_pinjam:
                print("Masukkan ID Buku Yang Sesuai!")
                id_buku_kembali = input("Masukkan ID Buku Yang Ingin Dikembalikan: ")
            else:    
                mycursor.execute("UPDATE daftar_pinjam SET TANGGAL_PENGEMBALIAN = %s WHERE ID_USER = %s \
                AND ID_BUKU = %s",(today, id_peminjam, id_buku_kembali))
                mycursor.execute("UPDATE daftar_buku SET STOCK = STOCK + 1 WHERE ID_BUKU=" + id_buku_kembali)
                mydb.commit()
                print("""
                Query berhasil dieksekusi
                ==========================
                Data Updated Successfully
                """)

        else:
            print("Belum Ada Peminjaman Buku")
                      
    except Error as err:
        print(f"Error: {err}")
