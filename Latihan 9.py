import random
from array import array

data_nilai_murid = []   

for i in range(10):
    nilai = random.randint(0, 100)  
    data_nilai_murid.append(nilai)   

print("Daftar Nilai Murid:")
for i in range(len(data_nilai_murid)):
    print("Mahasiswa", i+1, ":", data_nilai_murid[i])

rata_rata_nilai = sum(data_nilai_murid) / len(data_nilai_murid)

print("Rata-rata nilai:", rata_rata_nilai)

#2
import random
from array import array

data_id_karyawan = []   

for i in range(5):
    id  = random.randint(1000, 1500)  
    data_id_karyawan.append(id)   

print("Daftar ID karyawan:")
for i in range(len(data_id_karyawan)):
    print("Karyawan", i+1, ":", data_id_karyawan[i])

menu_data_karyawan = input(
"""MENU
1. Update ID
2. Hapus Semua Data ID """
)

match menu_data_karyawan:
    case "1":
        dataInputKaryawan = input("Masukan")
        data_id_karyawan.append(dataInputKaryawan)

#3
sistemPenyimpanan = []

# for i in range(5):
