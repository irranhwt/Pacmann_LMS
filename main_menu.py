#!/usr/bin/python3
import connection
import pendaftaran_user
import pendaftaran_buku
import peminjaman_buku
import display_buku
import display_user
import display_pinjam
import cari_buku
import pengembalian_buku


exit = False
while exit == False:

    menu = """
    ####################################################
    _________________LIBRARY MANAGEMENT_________________
    ####################################################

        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman
        4. Tampilkan Daftar Buku
        5. Tampilkan Daftar User
        6. Tampilkan Daftar/Riwayat Peminjaman
        7. Cari Buku
        8. Pengembalian
        9. Exit
    
    Masukkan Nomor Tugas:
    ----------------------------------------------------
    """
    tugas = input(menu)
    menu_tugas = ("1","2","3","4","5","6","7","8","9")  
    if tugas == "1":
        pendaftaran_user.daftar_user()
    elif tugas == "2":
        pendaftaran_buku.daftar_buku()
    elif tugas == "3":
        peminjaman_buku.pinjam_buku()
    elif tugas == "4":
        display_buku.buku_display()
    elif tugas == "5":
        display_user.user_display()
    elif tugas == "6":
        display_pinjam.pinjam_display()
    elif tugas == "7":
        cari_buku.search_buku()
    elif tugas == "8":
        pengembalian_buku.kembali()
    elif tugas == "9":
        exit = True
        print("""
              #########################################################
              _________Terima Kasih, Sampai Bertemu Kembali!___________
              #########################################################
        """)
    else:
        print("""!! Masukkan angka 1 sampai 9 : !!""")
    
    