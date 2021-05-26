import csv
import pandas as pd
import pyautogui

# Data
user = ("User")
password = ("01")


def cls():
    pyautogui.hotkey('ctrl', 'l')


def tampil_menu():
    cls()
    print(" ==================================================================")
    print(" ==================================================================")
    print("|                                                                  |")
    print("|                     Selamat Bertugas Pak RT                      |")
    print("|                                                                  |")
    print("|                  1. Data Warga                                   |")
    print("|                  2. Aspirasi Warga                               |")
    print("|                  3. Jadwal Kegiatan Bersama                      |")
    print("|                  4. Kembali ke login                             |")
    print("|__________________________________________________________________|")
    print("|__________________________________________________________________  |")
    pilih = input("\t\t   Silahkan Pilih Menu : ")
    print("")
    if pilih == "1":
        menu_warga()
    elif pilih == "2":
        menu_aspirasi()
    elif pilih == "3":
        menu_kegiatan()
    elif pilih == "4":
        menu_login()
    else:
        print("Pilihan Tidak Tersedia")
        tampil_menu()


# CRUD DATA WARGA
def menu_warga():
    cls()
    print("===================================================================")
    print("")
    read_warga()
    print("")
    print("===================================================================")
    print("     Diatas adalah data valid warga pada komplek yang anda urus!")
    print("===================================================================")
    print("|                            Menu :                                |")
    print("|                  1. Penambahan warga baru                        |")
    print("|                  2. Penghapusan  data  warga                     |")
    print("|                  3. Mengubah data warga                          |")
    print("|                  4. Kembali                                      |")
    print("")
    pilih = input("\t\t   Silahkan Pilih Menu : ")
    if pilih == "1":
        create_warga()
    elif pilih == "2":
        delete_warga()
    elif pilih == "3":
        update_warga()
    elif pilih == "4":
        tampil_menu()
    else:
        print("Pilihan Tidak Tersedia")
        menu_warga()


def read_warga():
    tampil = pd.read_csv('datakk.csv')
    print(tampil)


def delete_warga():
    cls()
    tampil = pd.read_csv("datakk.csv")
    read_warga()
    pilih = int(input("Pilih Indeks yang ingin dihapus : "))
    df = tampil.drop(pilih)
    df.to_csv("datakk.csv", index=False)
    print("Data Berhasil Dihapus")
    menu_warga()


def update_warga():
    cls()
    tampil = pd.read_csv("datakk.csv")
    read_warga()
    pilih = int(input("Pilih Indeks data warga yang ingin diubah : "))
    print("\t\tUPDATE DATA : ")
    tampil.loc[pilih, 'NIK'] = input("Masukkan NIK : ")
    tampil.loc[pilih, 'Nama'] = input("Masukkan Nama : ")
    tampil.loc[pilih, 'Tanggal Lahir'] = input("Masukkan Tanggal Lahir : ")
    tampil.loc[pilih, 'Tempat Lahir'] = input("Masukkan Tempat Lahir : ")
    tampil.loc[pilih, 'Agama'] = input("Masukkan Agama : ")
    tampil.to_csv("datakk.csv", index=False)
    cls()
    print("Data Sudah Diupdate!!!")
    menu_warga()


def create_warga():
    cls()
    data = []
    print("")
    print("===================================================================")
    read_warga()
    print("===================================================================")
    print("\t\t\tPENAMBAHAN WARGA :")
    NIK = input("Masukkan NIK : ")
    Nama = input("Masukkan Nama : ")
    Tanggal_lahir = input("Masukkan Tanggal Lahir : ")
    Tempat_lahir = input("Masukkan Tempat Lahir : ")
    Agama = input("Masukkan Agama : ")
    data.append(NIK)
    data.append(Nama)
    data.append(Tanggal_lahir)
    data.append(Tempat_lahir)
    data.append(Agama)
    d = open('datakk.csv', 'a', newline='')
    w = csv.writer(d)
    w.writerow(data)
    d.close()
    print("Data Sudah Ditambah!!!")
    print("")
    cls()
    data.clear()
    menu_warga()

# CRUD Data Aspirasi
def menu_aspirasi():
    cls()
    print(" ===================================================================")
    print(" ===================================================================")
    print("|                             Menu :                                |")
    print("|                   1. Liat Data Aspirasi Warga                     |")
    print("|                   2. Penghapusan  Data Aspirasi Warga             |")
    print("|                   3. Kembali                                      |")
    print("")
    pilih = input("\t\t  Silahkan Pilih Menu : ")
    if pilih == "1":
        print("")
        print("===================================================================")
        list_aspirasi()
        print("")
        print("===================================================================")
    elif pilih == "2":
        delete_aspirasi()
    elif pilih == "3":
        tampil_menu()
    else:
        print("Pilihan Tidak Tersedia")
        menu_aspirasi()


def list_aspirasi():
    tampil = pd.read_csv("dataaspirasi.csv")
    print(tampil)

def delete_aspirasi():
    cls()
    tampil = pd.read_csv("dataaspirasi.csv")
    list_aspirasi()
    pilih = int(input("Pilih Indeks yang ingin dihapus : "))
    df = tampil.drop(pilih)
    df.to_csv("dataaspirasi.csv", index=False)
    print("Data Berhasil Dihapus")
    menu_aspirasi()


# CRUD Kegiatan Warga
def menu_kegiatan():
    cls()
    print(" ===================================================================")
    read_kegiatan()
    print(" ===================================================================")
    print("        Diatas adalah data kegiatan yang akan terjadi di RT !")
    print(" ===================================================================")
    print("|                            Menu :                                 |")
    print("|                  1. Penambahan kegiatan baru                      |")
    print("|                  2. Penghapusan  kegiatan                         |")
    print("|                  3. Mengubah data kegiatan                        |")
    print("|                  4. Kembali                                       |")
    print("")
    pilih = input("\t\t\t\t\t   Silahkan Pilih Menu : ")
    if pilih == "1":
        create_kegiatan()
    elif pilih == "2":
        delete_kegiatan()
    elif pilih == "3":
        update_kegiatan()
    elif pilih == "4":
        tampil_menu()
    else:
        print("Pilihan Tidak Tersedia")
        menu_kegiatan()


def read_kegiatan():
    tampil = pd.read_csv("datakegiatan.csv")
    print(tampil)


def delete_kegiatan():
    cls()
    tampil = pd.read_csv("datakegiatan.csv")
    read_kegiatan()
    pilih = int(input("Pilih Indeks yang ingin dihapus : "))
    df = tampil.drop(pilih)
    df.to_csv("datakegiatan.csv", index=False)
    print("Data Berhasil Dihapus")
    menu_kegiatan()


def update_kegiatan():
    cls()
    tampil = pd.read_csv("datakegiatan.csv")
    read_kegiatan()
    pilih = int(input("Pilih Indeks data kegiatan yang ingin diubah : "))
    print("\t\tUPDATE DATA : ")
    tampil.loc[pilih, 'Tanggal'] = input("Masukkan Tanggal : ")
    tampil.loc[pilih, 'Nama Kegiatan'] = input("Masukkan Nama : ")
    tampil.loc[pilih, 'Waktu'] = input("Masukkan Waktu : ")
    tampil.to_csv("datakegiatan.csv", index=False)
    cls()
    print("Data Sudah Diupdate!!!")
    menu_kegiatan()


def create_kegiatan():
    cls()
    data = []
    print("")
    print("===================================================================")
    read_kegiatan()
    print("===================================================================")
    Tanggal = input("Masukkan Tanggal Kegiatan : ")
    Nama = input("Masukkan Nama Kegiatan : ")
    Waktu = input("Masukkan Waktu Kegiatan : ")
    data.append(Tanggal)
    data.append(Nama)
    data.append(Waktu)
    d = open('datakegiatan.csv', 'a', newline='')
    w = csv.writer(d)
    w.writerow(data)
    d.close()
    print("Data Sudah Ditambah!!!")
    print("")
    cls()
    data.clear()
    menu_kegiatan()


# Menu Login
def menu_login():
    cls()
    print(" ==================================================================")
    print(" ==================================================================")
    print("|                                                                 |")
    print("|                     Selamat Datang !!!                          |")
    print("|                                                                 |")
    print("|                        1. Pak RT                                |")
    print("|                        2. Warga                                 |")
    print("|                        3. Keluar                                |")
    print("|_________________________________________________________________|")
    print("")
    pilih = input("\t\t\t\t\t   Silahkan Pilih Menu : ")
    if pilih == "1":
        login = input("\t\t\t\t\t   Silahkan Masukkan Username : ")
        pw = input("\t\t\t\t\t   Silahkan Masukkan Password : ")
        if (login == user and pw == password):
            tampil_menu()
        else:
            print("Username atau Password Salah")
            menu_login()
    elif pilih == "2":
        tampil_warga()


# Menu Warga
def tampil_warga():
    print(" ==================================================================")
    print(" ==================================================================")
    print("|                                                                 |")
    print("|                    Halo Warga !!!                               |")
    print("|                                                                 |")
    print("|                  1. Liat Data Warga                             |")
    print("|                  2. Liat Kegiatan RT                            |")
    print("|                  3. Memberi Aspirasi                            |")
    print("|                  4. Kembali ke login                            |")
    print("|_________________________________________________________________|")
    print("")
    pilih = input("\t\t\t\t\t   Silahkan Pilih Menu : ")
    if pilih == "1":
        read_warga()
        tampil_warga()
    elif pilih == "2":
        read_kegiatan()
        tampil_warga()
    elif pilih == "3":
        beri_aspirasi()
    elif pilih == "4":
        menu_login()


def beri_aspirasi():
    data = []
    print("")
    print("===================================================================")
    print("                 Silahkan Berikan Aspirasi Anda                    ")
    print("===================================================================")
    NIK = input("Silahkan isi NIK anda : ")
    nama = input("Silahkan isi nama anda : ")
    aspirasi = input("Silahkan Berikan Aspirasi Kalian : ")
    data.append(NIK)
    data.append(nama)
    data.append(aspirasi)
    d = open('dataaspirasi.csv', 'a', newline='')
    w = csv.writer(d)
    w.writerow(data)
    d.close()
    print("Aspirasi anda sudah berhasil disampaikan !!!")
    print("")
    cls()
    data.clear()
    tampil_warga()


menu_login()