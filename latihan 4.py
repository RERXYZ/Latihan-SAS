def cek_barang(gudang, nama_barang):
    if nama_barang in gudang:
        print(f"Barang tersedia, stok: {gudang[nama_barang]}")
    else:
        print("Barang tidak ditemukan")


# contoh penggunaan
gudang = {"nasi": 10, "mie": 5, "teh": 8}
cek_barang(gudang, "mie")   
cek_barang(gudang, "kopi")  
