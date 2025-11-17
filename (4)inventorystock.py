def cek_barang(inventory, product_name):
    if product_name in inventory:
        print(f"Barang tersedia Pak Bos, sisa stok ada: {inventory[product_name]}")
    else:
        print("Barang tidak ditemukan Pak Bos")

inventory = {"nasi": 10, "mie": 5, "teh": 8}

cek_barang(inventory, "mie")   
cek_barang(inventory, "kopi")  