import connection
from mysql.connector import Error
import datetime

def daftar_user():
    """
    melakukan insert data user ke database daftar_user
    
    Parameter:
        nama_user = input nama user (str)
        tgl_lahir = input tgl_lahir (date)
        pekerjaan = input pekerjaan (str)
        alamat = input alamat (str)
        
    Returns:
        database daftar_user updated
        
    """
    nama_user = input("Masukkan Nama User: ")
    
    while True :
        tgl_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
        try :
            tgl_lahir = datetime.datetime.strptime(tgl_lahir, "%Y-%m-%d")
            break
        except ValueError:
            print("Error: masukkan sesuai format YYYY-MM-DD ")
    
    pekerjaan = input("Masukkan Pekerjaan: ")
    alamat = input("Masukkan Alamat: ")
    data = (nama_user, tgl_lahir, pekerjaan, alamat)
    
    try:
        query = """INSERT INTO daftar_user(U_NAME,TGL_LAHIR,PEKERJAAN,ALAMAT) VALUES(%s,%s,%s,%s)"""
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