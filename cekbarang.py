def cek_barang(gudang, nama_barang):
    if nama_barang in gudang:
        print(f"Barang tersedia, stok: {gudang[nama_barang]}")
    else:
        print("Barang tidak ditemukan")
