#1
input_number_of_cups_lemonade_sold = int(input("Berapa gelas lemon yang telah terjual:"))
lemonade = int(2)
profit_of_number_of_cups_lemonade_sold = input_number_of_cups_lemonade_sold * lemonade
print("Keuntungan Jack adalah: $", profit_of_number_of_cups_lemonade_sold)

#2
input_total_number_of_flower = int(input("Berapa Total Bunga: "))
modulo = input_total_number_of_flower // 6
print("Jumlah baris yang dapat dibentuk adalah: ", modulo)

#3
input_guest = int(input("Berapa Jumlah tamu yang akan datang? "))
pizza_for_feed = 8
pizza_to_buy = input_guest / pizza_for_feed
print("Maka Pizza yang dibutuhkan adalah {}".format(pizza_to_buy))

#4
input_book_price = int(input("Harga Buku: Rp."))
diskon = 0.25
jumlah_diskon = input_book_price * diskon
jumlah_akhir = input_book_price - jumlah_diskon
print("Harga setelah dipotong diskon adalah Rp.{}".format(int(jumlah_akhir)))

#5
input_total_pinjam_hari = int(input("Berapa hari meminjam buku nya?"))
modulo_minggu = input_total_pinjam_hari % 7
list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum`at", "Sabtu", "Minggu"]
print("Anda Harus mengembalikan Buku ini di Hari {}".format(list_hari[modulo_minggu]))