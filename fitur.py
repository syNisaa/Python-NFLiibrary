import random, string

print("Selamat Datang Di NF Library")   


while True:
    print("Silahkan Pilih Menu : \n [1] Tambah Anggota Baru \n [2] Tambah Buku Baru \n [3] Pinjam Buku \n [4] Kembalikan Buku \n [5] Lihat data Anggota \n [6] Lihat Data Pinjaman [7] Keluar")
    pilihan = input("Masukan Menu Pilihan Anda : ")

    # Fitur 1 : Pendaftaran Anggota
    if pilihan == "1":
        print(" *** Pendaftaran Angoota Baru ***")
        namaAnggota = input("Masukan nama : ")
        while True:
            status = input("Apakah Salah Satu Karyawan NF Group ? [Y/T] : ")
            print(status)
            if status.upper() == "Y":
                status = "1"
                break
            elif status.upper() == "T":
                status = "2"
                break
            else:
                print("Inputan berupa [Y / T]")
        # pass
        kode = "LNF" + ''.join(random.choice(string.digits) for _ in range(3))
        myAnggota = open("NFLibrary/anggota.txt", 'a+')
        myAnggota.write("\n"+kode +","+namaAnggota+","+status)
        myAnggota.close()
        print("Pendaftaran anggota dengan kode" , kode , "atas nama", namaAnggota, "berhasil.")
        
    # Fitur Menambah Buku
    elif pilihan == "2":
        pass
        break

    # Fitur Meminjam Buku
    elif pilihan == "3":
        pass
        break

    # Fitur Pengembalian Buku
    elif pilihan == "4":
        pass
        break

    # Fitur Melihat Daftar Anggota 
    elif pilihan == "5":
        f = open('NFLibrary/anggota.txt')
        print("Daftar Anggota Yang Terdaftar : ")
        for each_line in f:
            print(each_line.strip())
        f.close()
 
        break

    # Fitur 6 Melihat data Peminjaman Buku
    elif pilihan == "6":
        pass
        break

    # Fitur 7 : Selesai
    elif pilihan == "7":
        print("Terimakasih Atas Kunjungan Anda, Silahkan Datang Kembali...")
        break

    # Pilihan yang tidak ada
    else:
        print("Pilihan yang ada masukan tidak ada.")
