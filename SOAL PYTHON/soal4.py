# Fungsi untuk mengecek ketersediaan barang di gudang
def cek_barang(gudang, nama_barang):
    if nama_barang in gudang:
        print("Barang tersedia, stok:", gudang[nama_barang])
    else:
        print("Barang tidak ditemukan")

# Contoh penggunaan
gudang = {"nasi": 10, "mie": 5, "teh": 8}
cek_barang(gudang, "mie")
cek_barang(gudang, "kopi")
cek_barang(gudang, "nasi")
cek_barang(gudang, "teh")
cek_barang(gudang, "gula")
cek_barang(gudang, "garam")
cek_barang(gudang, "minyak")
cek_barang(gudang, "beras")