# Fungsi untuk menghitung total harga dari sebuah dictionary
def total_harga(data):
    total = 0
    for harga in data.values():
        total += harga
    print("Total harga semua barang:", total)

# Contoh 1
barang = {"apel": 5000, "mangga": 7000, "jeruk": 8000}
total_harga(barang)

# Contoh 2
barang2 = {"pisang": 6000, "kiwi": 9000}
total_harga(barang2)

# Contoh 3
barang3 = {"anggur": 12000, "semangka": 15000,"melon": 10000}
total_harga(barang3)

# Contoh 4
barang4 = {"nanas": 11000, "pepaya": 9500, "sirsak": 13000}
total_harga(barang4)