nilai = []

while  True:

    UserInput = input("""
Pilih Menu
1. Tambah Data
2. Pengaturan
3. Exit          
    """)

    match UserInput:
        case "1":
            dataInput = int(input("Masukan Datanya "))
            nilai.append(dataInput)
            print(nilai)
        case "2":
            PenganturanInput = input("""
1. Profil
2. Data Diri
3. Exit                         
            """)

            match PenganturanInput:
                case "1":
                    print("Profil Anda")
                case "2":
                    print("Data Diri Anda")
                case _:
                    print("kembali")
        case "3":
            print("Anda telah LogOut")
            break
        case _:
            print("Input anda salah")