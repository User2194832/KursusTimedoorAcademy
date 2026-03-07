#1
input_number = int(input("Masukan nilai:"))
i = 0
while input_number >= 1:
    print(i+1, end=" ")
    i += 1
    input_number -= 1

#2
Angka = 78
while True:
    guest_number = int(input("Masukan Angka:"))
    if guest_number == Angka:
        print("Selamat, Tebakan Anda Benar!")
        break
    elif guest_number > Angka:
        print("Nilai anda lebih tinggi!")
    else:
        print("Nilai anda lebih rendah!")

#3
n_max = 7
n_1, n_2 = 0,1
count = 0 
while count < n_max:
    print(n_1)
    adh = n_1 + n_2
    n_1 = n_2
    n_2 = adh
    count += 1

#4
Password = 123456
while True:
    input_password = int(input("Masukan Password Anda:"))
    if input_password == Password:
        print("Selamat Password Anda Benar!")
        break
    else:
        print("Password Anda Salah!")

#5
for i in range(20):
    if i % 2 == 0:
        continue 
    elif i % 3 == 0:
        print("Nilai tersebut dapat dibagi oleh 3")
        continue
    elif i % 5 == 0:
        print("Nilai tersebut dapat dibagi oleh 5")
        continue
    else:
        print(i)