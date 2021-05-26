from prettytable import PrettyTable
import csv

df = open('dataaspirasi.csv', 'w+')
# create the csv writer
writer = csv.writer(df)
reader = csv.reader(df)
# write a row to the csv file
list_aspirasi = list(reader)
writer.writerow()

def linearSearch(array, n, x):
    for i in range(0, n):
        if (x in array[i]):
            return i
    return -1

def sublistlinearSearch(array, n, x):
    for i in range(0, n):
        if (x == array[i]):
            return i
    return -1

def drivercode():
    x = int(input("Cari tanggal : "))
    n = len(list_aspirasi)
    result = linearSearch(list_aspirasi, n, x)
    if (result == -1):
        print("Data tidak ditemukan.")
    else:
        result2 = sublistlinearSearch(list_aspirasi[result], n, x)
        print(result2)

drivercode()

