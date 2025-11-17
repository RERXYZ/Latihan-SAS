def total_harga(data):
    total = sum(data.values())
    print(f"Total harga semua barang: {total}")


# contoh penggunaan
barang = {"apel": 5000, "mangga": 7000, "jeruk": 8000}
total_harga(barang)  
