#Meeting 2
num = 42
pi = 3.14159

print(f"Integer: {num} hanya satu string {pi}")
print("Integers:" ,num, "ini isinya perlu 2 string")
#Kalau pakai F lebih gampang memasukan variabel dalam string dengan {} sedangkan tidak pakai f harus manggil string dengan , (koma)
print("Float: {:.2f}".format(pi))

#Mencari Character dengan urutan index
my_string = "Hello, World!"
char_at_index = my_string[0]
print(char_at_index)

#Mengubah Hasil Tampilan menjadi huruf kecil semua
my_string = "Hello, World!"
lowercase_string = my_string.lower()
print(lowercase_string)

#Mengubah Hasil Tampilan menjadi huruf besar semua
my_string = "Hello, World!"
uppercase_string = my_string.upper()
print(uppercase_string)

#Concat String
string1 = "Hello, "
string2 = "World!"
concatenated_string = string1 + string2
print(concatenated_string)

#Slice String
input_string = "Hello, World!"
start_index = 3
end_index = 8
sliced_string = input_string[start_index:end_index]
print(sliced_string)

Angka1 = 80.61781
Angka2 = 50.78013

print("Angka Kamu adalah {:.2f}".format(Angka1), "Angka Kedua Kamu adalah {:.3f}".format(Angka2))


print(f"Angka Pertama kamu adalah = {Angka1} dan Angka Kedua Kamu adalah {Angka2}")