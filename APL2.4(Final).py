import os
import time

Username = ("Rizky")
Password = ('123231')
Januari = [[12000,12],
            [56000,14],
            [30000,16],
            [12000,11],
            [60000,7],
            [30000,6]]
Februari = [[61500,10],
         [95100,9],
         [45000,12],
         [13000,7],
         [60000,15],
         [70000,6],]
Maret = [[215000,8],
         [415000,9],
         [514000,18],
         [180000,24],
         [160000,27],
         [710000,3]]
April = [[190000,28],
         [280000,6],
         [980000,3],
         [716500,1],
         [613400,8],
         [800500,9]]
Mei = [[780000,4],
         [413000,31],
         [430000,30],
         [514000,3],
         [678000,18],
         [142000,19]]
Juni = [[125000,4],
         [617500,9],
         [312000,18],
         [900500,24],
         [743000,27],
         [809500,3]]
Juli = [[900000,12],
         [617500,6],
         [413000,3],
         [613400,1],
         [980000,8],
         [142000,9]]
Agustus = [[900000,7],
         [980000,31],
         [142000,30],
         [800500,3],
         [780000,18],
         [125000,19]]
September = [[115000,19],
         [65000,5],
         [71000,4],
         [44000,1],
         [89000,2],
         [12500,16]]
Oktober = [[130000,12],
         [110000,6],
         [120000,9],
         [160000,27],
         [140000,21],
         [150000,23],]
November = [[116000,11],
         [111000,6],
         [112000,9],
         [121000,29],
         [118000,26],
         [129000,31],]
Desember = [[67000,22],
         [68000,30],
         [69000,3],
         [70000,12],
         [71000,16],
         [72000,7]]

def menu():
    cls()
    print(" _____________________________________")
    print("|                                     |")
    print("|                MENU                 |")
    print("|_____________________________________|")
    print("|                                     |")
    print("| 1. Lihat Data Pengeluaran           |")
    print("| 2. Hapus Data Pengeluaran           |")
    print("| 3. Ubah Data Pengeluaran            |")
    print("| 4. Tambah Data Pengeluaran          |")
    print("| 5. Sorting Pengeluaran              |")
    print("| 6. Cari Data Pengeluaran            |")
    print("| 7. Exit                             |\n")
    pilih = int(input("Pilih Menu : "))
    if pilih == 1:
        show()
    elif pilih == 2:
        delete()
    elif pilih == 3:
        change()
    elif pilih == 4:
        tambah()
    elif pilih == 5:
        sorting()
    elif pilih == 7:
        print("Terima Kasih")
        time.sleep(1.3)
        login()
    elif pilih == 6:
        menu_search()
    else:
        input("Menu tidak ada, tekan enter untuk melanjutkan...")

# Menu No. 1 (Melihat data)
def show():
    cls()
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    print("+"*25)
    if pilih_bulan == "1":
        print("Nominal      Tanggal")
        for a in range(len(Januari)):
            for b in range(len(Januari[a])):
                print(Januari[a][b], end = "           ")
            print()
        input("...")
    if pilih_bulan == "2":
        print("Nominal      Tanggal")
        for a in range(len(Februari)):
            for b in range(len(Februari[a])):
                print(Februari[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "3":
        print("Nominal      Tanggal")
        for a in range(len(Maret)):
            for b in range(len(Maret[a])):
                print(Maret[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "4":
        print("Nominal      Tanggal")
        for a in range(len(April)):
            for b in range(len(April[a])):
                print(April[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "5":
        print("Nominal      Tanggal")
        for a in range(len(Mei)):
            for b in range(len(Mei[a])):
                print(Mei[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "6":
        print("Nominal      Tanggal")
        for a in range(len(Juni)):
            for b in range(len(Juni[a])):
                print(Juni[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "7":
        print("Nominal      Tanggal")
        for a in range(len(Juli)):
            for b in range(len(Juli[a])):
                print(Juli[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "8":
        print("Nominal      Tanggal")
        for a in range(len(Agustus)):
            for b in range(len(Agustus[a])):
                print(Agustus[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "9":
        print("Nominal      Tanggal")
        for a in range(len(September)):
            for b in range(len(September[a])):
                print(September[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "10":
        print("Nominal      Tanggal")
        for a in range(len(Oktober)):
            for b in range(len(Oktober[a])):
                print(Oktober[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "11":
        print("Nominal      Tanggal")
        for a in range(len(November)):
            for b in range(len(November[a])):
                print(November[a][b], end = "            ")
            print()
        input("...")
    if pilih_bulan == "12":
        print("Nominal      Tanggal")
        for a in range(len(Desember)):
            for b in range(len(Desember[a])):
                print(Desember[a][b], end = "            ")
            print()
        input("...")
    menu()
 
def view_bulan():
    print("1.  Januari")
    print("2.  Februari")
    print("3.  Maret")
    print("4.  April")
    print("5.  Mei")
    print("6.  Juni")
    print("7.  Juli")
    print("8.  Agustus")
    print("9.  September")
    print("10. Oktober")
    print("11. November")
    print("12. Desember")

# Menu No. 2 (Menghapus data)
def delete():
    cls()
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    if pilih_bulan == "1":
        cek_tanggal = len(Januari) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Januari[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Januari[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "2":
        cek_tanggal = len(Februari) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Februari[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Februari[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "3":
        cek_tanggal = len(Februari) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Februari[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Februari[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "4":
        cek_tanggal = len(April) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == April[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del April[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "5":
        cek_tanggal = len(Mei) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Mei[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Mei[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "6":
        cek_tanggal = len(Juni) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Juni[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Juni[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "7":
        cek_tanggal = len(Juli) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Juli[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Juli[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "8":
        cek_tanggal = len(Agustus) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Agustus[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Agustus[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "9":
        cek_tanggal = len(September) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == September[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del September[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "10":
        cek_tanggal = len(Oktober) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Oktober[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Oktober[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "11":
        cek_tanggal = len(November) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == November[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del November[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "12":
        cek_tanggal = len(Desember) - 1
        hapus_tanggal = int(input("Masukkan tanggal data yang ingin dihapus : "))
        while (cek_tanggal >= 0):
            if hapus_tanggal == Desember[cek_tanggal][1]:
                break
            else:
                cek_tanggal -= 1
        if (cek_tanggal >= 0):
            del Desember[cek_tanggal]
            print("Berhasil menghapus data!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Tanggal tidak ada dalam data\n")
            time.sleep(1.5)
            menu()

# Menu No. 3 (Mengubah data)
def change():
    cls()
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    if pilih_bulan == "1":
        cek_tanggal = len(Januari) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Januari[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Januari[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Januari[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "2":
        cek_tanggal = len(Februari) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Februari[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Februari[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Februari[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "3":
        cek_tanggal = len(Maret) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Maret[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Maret[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Maret[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "4":
        cek_tanggal = len(April) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == April[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            April[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            April[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "5":
        cek_tanggal = len(Mei) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Mei[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Mei[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Mei[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "6":
        cek_tanggal = len(Juni) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Juni[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Juni[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Juni[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "7":
        cek_tanggal = len(Juli) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Juli[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Juli[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Juli[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "8":
        cek_tanggal = len(Agustus) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Agustus[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Agustus[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Agustus[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "9":
        cek_tanggal = len(September) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == September[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            September[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            September[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "10":
        cek_tanggal = len(Oktober) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Oktober[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Oktober[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Oktober[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "11":
        cek_tanggal = len(November) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == November[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            November[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            November[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()
    if pilih_bulan == "12":
        cek_tanggal = len(Desember) - 1
        change_data = int(input("Masukkan tanggal yang ingin diganti : "))
        print('-'*10)
        while(cek_tanggal >=0):
            if (change_data == Desember[cek_tanggal][1]):
                break
            else:
                cek_tanggal -= 1
        if  (cek_tanggal >= 0):
            up_data1 = int(input("Masukkan nominal : "))
            Desember[cek_tanggal][0] = up_data1
            up_data2 = int(input("Masukkan tanggal : "))
            Desember[cek_tanggal][1] = up_data2
            print("Data berhasil diubah!!!")
            print("="*10)
            time.sleep(1.5)
            menu()
        else:
            print("Maaf,tanggal tidak tersedia")
            time.sleep(1.5)
            menu()

# Menu No. 4 (Menambah data)
def tambah():
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    if pilih_bulan == "1":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Januari.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "2":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Februari.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "3":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Maret.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "4":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = April.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "5":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Mei.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "6":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Juni.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "7":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Juli.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "8":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Agustus.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "9":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = September.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "10":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Oktober.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "11":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = November.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()
    if pilih_bulan == "12":
        cls()
        tambah_tanggal = int(input("Masukkan tanggal : "))
        tambah_nominal = int(input("Masukkan nominal : "))
        tambah_ = Desember.append([tambah_nominal,tambah_tanggal])
        print("Data berhasil ditambah!!!")
        print("="*10)
        time.sleep(1.5)
        menu()

# Menu No. 5 (Sortir data) Bubble Sort
def sorting():
    print("Mensorting tanggal secara ascending dan descending")
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    if pilih_bulan == "1":
        sort_januari()
    if pilih_bulan == "2":
        sort_februari()
    if pilih_bulan == "3":
        sort_maret()
    if pilih_bulan == "4":
        sort_april()
    if pilih_bulan == "5":
        sort_mei()
    if pilih_bulan == "6":
        sort_juni()
    if pilih_bulan == "7":
        sort_juli()
    if pilih_bulan == "8":
        sort_agustus()
    if pilih_bulan == "9":
        sort_september()
    if pilih_bulan == "10":
        sort_oktober()
    if pilih_bulan == "11":
        sort_november()
    if pilih_bulan == "12":
        sort_desember()

def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def sort_januari():
    Sort(Januari)
    print('='*25)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Januari)):
        for b in range(len(Januari[a])):
            print(Januari[a][b], end = "            ")
        print()
    Januari.reverse()
    print('='*25)
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Januari)):
        for b in range(len(Januari[a])):
            print(Januari[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_februari():
    Sort(Februari)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Februari)):
        for b in range(len(Februari[a])):
            print(Februari[a][b], end = "            ")
        print()
    Februari.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Februari)):
        for b in range(len(Februari[a])):
            print(Februari[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_maret():
    Sort(Maret)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Maret)):
        for b in range(len(Maret[a])):
            print(Maret[a][b], end = "            ")
        print()
    Maret.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Maret)):
        for b in range(len(Maret[a])):
            print(Maret[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_april():
    Sort(April)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(April)):
        for b in range(len(April[a])):
            print(April[a][b], end = "            ")
        print()
    April.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(April)):
        for b in range(len(April[a])):
            print(April[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_mei():
    Sort(Mei)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Mei)):
        for b in range(len(Mei[a])):
            print(Mei[a][b], end = "            ")
        print()
    Mei.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Mei)):
        for b in range(len(Mei[a])):
            print(Mei[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_juni():
    Sort(Juni)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Juni)):
        for b in range(len(Juni[a])):
            print(Juni[a][b], end = "            ")
        print()
    Juni.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Juni)):
        for b in range(len(Juni[a])):
            print(Juni[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_juli():
    Sort(Juli)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Juli)):
        for b in range(len(Juli[a])):
            print(Juli[a][b], end = "            ")
        print()
    Juli.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Juli)):
        for b in range(len(Juli[a])):
            print(Juli[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_agustus():
    Sort(Agustus)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Agustus)):
        for b in range(len(Agustus[a])):
            print(Agustus[a][b], end = "            ")
        print()
    Agustus.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Agustus)):
        for b in range(len(Agustus[a])):
            print(Agustus[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_september():
    Sort(September)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(September)):
        for b in range(len(September[a])):
            print(September[a][b], end = "            ")
        print()
    September.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(September)):
        for b in range(len(September[a])):
            print(September[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_oktober():
    Sort(Oktober)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Oktober)):
        for b in range(len(Oktober[a])):
            print(Oktober[a][b], end = "            ")
        print()
    Oktober.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Oktober)):
        for b in range(len(Oktober[a])):
            print(Oktober[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_november():
    Sort(November)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(November)):
        for b in range(len(November[a])):
            print(November[a][b], end = "            ")
        print()
    November.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(November)):
        for b in range(len(November[a])):
            print(November[a][b], end = "            ")
        print()
    input('...')
    menu()
def sort_desember():
    Sort(Desember)
    print ("List Data Secara Ascending :")
    print("Nominal      Tanggal")
    for a in range(len(Desember)):
        for b in range(len(Desember[a])):
            print(Desember[a][b], end = "            ")
        print()
    Desember.reverse()
    print ("List Data Secara Descending :")
    print("Nominal      Tanggal")
    for a in range(len(Desember)):
        for b in range(len(Desember[a])):
            print(Desember[a][b], end = "            ")
        print()
    input('...')
    menu()

# Menu No. 7 (Searching)
# Linear Search
def menu_search():
    print("1. Linear Search")
    pilih_search = input("Pilih metode sorting : ")
    if pilih_search == "1":
        drivercode()
def linearSearch(array, n, x):
    for i in range(0, n):
        if (x in array[i]):
            return i
    return -1
def drivercode():
    view_bulan()
    pilih_bulan = input("Pilih bulan : ")
    if pilih_bulan == "1":
       pilih_bulan = Januari
    elif pilih_bulan == "2":
       pilih_bulan = Februari
    elif pilih_bulan == "3":
       pilih_bulan = Maret 
    elif pilih_bulan == "4":
       pilih_bulan = April 
    elif pilih_bulan == "5":
       pilih_bulan = Mei 
    elif pilih_bulan == "6":
       pilih_bulan = Juni
    elif pilih_bulan == "7":
       pilih_bulan = Juli 
    elif pilih_bulan == "8":
       pilih_bulan = Agustus
    elif pilih_bulan == "9":
       pilih_bulan = September
    elif pilih_bulan == "10":
       pilih_bulan = Oktober
    elif pilih_bulan == "11":
       pilih_bulan = November
    elif pilih_bulan == "12":
       pilih_bulan = Desember
    x = int(input("Cari tanggal : "))
    n = len(Januari)
    result = linearSearch(Januari, n, x)
    if(result == -1):
        print("Data tidak ditemukan.")
    else:
        print("Data ditemukan pada index : ", result)
        print("Nominal      Tanggal")
        for a in range(len(pilih_bulan)):
            for b in range(len(pilih_bulan[a])):
                print(pilih_bulan[a][b], end = "            ")
            print()
            time.sleep(1.5)
    menu()

# Login
def login():
    cls()
    print("|\t   Catatan Pengeluaran Tahun 2020    \t|")
    print("\t             1. Login")
    print("\t             2. Exit")
    pilihlogin = input("Pilih : ")
    if pilihlogin == "1":
        username = input("\t        Username : ")
        password = input("\t        Password : ")
        if username == Username and password == Password:
            print("\n\n\t     Selamat anda berhasil masuk!")
            time.sleep(1)
            menu()
        else:
            print(" Username atau password salah silakan ulangi lagi")
            time.sleep(1)
            login()
    elif pilihlogin == "2":
        print("      Terima kasih sudah menggunakan program ini!")
def cls():
    os.system("cls" if os.name == "nt" else "clear")

login()