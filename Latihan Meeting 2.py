#1
InputData = input("Masukan Nama Anda:")
StartIndex 
print("Nama Anda", InputData)
#Salah kurang konsep Index

#2
InputNama = input("Masukan Nama Kamu:")
HasilInputNama = InputNama.lower()
print("Nama Kamu adalah:" ,HasilInputNama)

#3
InputNamaAnda = input("Masukan Nama Anda:")
HasilInputNamaAnda = InputNamaAnda.upper()
print("Nama Anda Adalah:", HasilInputNamaAnda)

#4
NamaDepan = "Ali"
NamaBelakang = "Umar"
print("Nama nya adalah", NamaDepan + NamaBelakang)
#Harus nya Input variabel

#5
InputNamaMahasiswa = input("Masukan Nama Anda:")
HasilInputNamaMahasiswa = InputNamaMahasiswa
StartIndex = 3
EndIndex = 5
SlicedString = HasilInputNamaMahasiswa[StartIndex:EndIndex]
print("Kode Nama nya adalah:" ,SlicedString)
#Star Index dan End Index harus nya Input dari user lalu ubah ke interger

#6
pi = 3.14159
InputKeteranganLingkaran = float(input("Masukan Nilai Radius Lingkaran:"))
RumusLuasLingkaran = pi * (InputKeteranganLingkaran * InputKeteranganLingkaran)
HasilInputKeteranganLingkaran = RumusLuasLingkaran
print("Luas Lingkaran Adalah: {:.2f}".format(HasilInputKeteranganLingkaran))

#umum nya variabel pakai Camel Case
#umum nya tabel pakai Snake Case
#umum nya class pakai Pascal Case
