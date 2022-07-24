import mysql.connector 
from mysql.connector import Error

def connect():
    """
    membuat koneksi ke mysql
    
    Parameter:
        nama_host 
        user
        password
        db
        
    Returns:
        mydb
    
    """
    nama_host = "localhost" 
    user = "user_new" 
    password = "" 
    db = "LMS" 
    try:
        mydb = mysql.connector.connect(host = nama_host, user = user, passwd = password, database = db)
    except Error as err:
        print(f"Error: {err}")
    return mydb
    
