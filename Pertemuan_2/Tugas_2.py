from abc import ABC, abstractmethod

# Kelas abstrak Produk
class Produk(ABC):
    _nama_toko = "Toko Rojak Bahagia"

    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    # Getter
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Setter
    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_harga(self, harga_baru):
        self.__harga = harga_baru

    # Abstract method
    @abstractmethod
    def get_informasi(self):
        pass

    # Class method
    @classmethod
    def get_toko_nama(cls):
        return cls._nama_toko

    # Static method
    @staticmethod
    def format_uang(amount):
        return f"Rp. {amount:,}".replace(",", ".")

    # __str__ untuk mencetak informasi produk
    def __str__(self):
        return self.get_informasi()

    # __add__ untuk menambahkan harga dua produk
    def __add__(self, other):
        if isinstance(other, Produk):
            return self.get_harga() + other.get_harga()
        return NotImplemented

# Subclass Makanan
class Makanan(Produk):
    def __init__(self, nama, harga, pedas):
        super().__init__(nama, harga)
        self._pedas = pedas

    def get_informasi(self):
        pedas = "Pedas" if self._pedas else "Tidak pedas"
        return f"Makanan {self.get_nama()} | {pedas} | Harga = {self.format_uang(self.get_harga())}"

# Subclass Minuman
class Minuman(Produk):
    def __init__(self, nama, harga, dingin):
        super().__init__(nama, harga)
        self._dingin = dingin

    def get_informasi(self):
        dingin = "Dingin" if self._dingin else "Hangat"
        return f"Minuman {self.get_nama()} | {dingin} | Harga = {self.format_uang(self.get_harga())}"

# Kelas untuk interaksi transaksi
class Berinteraksi:
    def __init__(self):
        self._barang = []

    def tambahkan_barang(self, item):
        self._barang.append(item)

    def total_harga(self):
        total = sum(item.get_harga() for item in self._barang)
        return total

    def struk_harga(self):
        print("\n=========== STRUK BELANJA ANDA ===========")
        print(f"Toko: {Produk.get_toko_nama()}")
        for item in self._barang:
            print("-", item)
        print("Total bayar =", Produk.format_uang(self.total_harga()))
        print("==========================================\n")

# Fungsi utama
def main():
    transaksi = Berinteraksi()
    while True:
        print("\n======= MENU TOKO ROJAK BAHAGIA =======")
        print("1. Beli Makanan")
        print("2. Beli Minuman")
        print("3. Lihat Struk Belanja")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\n---- DAFTAR MAKANAN ----")
            print("1. Pizza with foie gras and caviar (Rp 1.000.000)")
            print("2. King Crab Alaska (Rp 5.000.000)")
            print("3. Wagyu A5 (Rp 500.000)")
            print("4. Mie Ayam (Rp 10.000)")
            print("5. Nasi Padang (Rp 20.000)")
            hidangan = input("Pilih hidangan: ")
            if hidangan == "1":
                transaksi.tambahkan_barang(Makanan("Pizza with foie gras and caviar", 1000000, False))
            elif hidangan == "2":
                transaksi.tambahkan_barang(Makanan("King Crab Alaska", 5000000, True))
            elif hidangan == "3":
                transaksi.tambahkan_barang(Makanan("Wagyu A5", 500000, False))
            elif hidangan == "4":
                transaksi.tambahkan_barang(Makanan("Mie Ayam", 10000, False))
            elif hidangan == "5":
                transaksi.tambahkan_barang(Makanan("Nasi Padang", 20000, True))
            else:
                print("Pilihan tidak valid!")
        elif pilihan == "2":
            print("\n--- DAFTAR MINUMAN ---")
            print("1. Es Teh (Rp 8.000)")
            print("2. Teh Hangat (Rp 7.000)")
            print("3. Mojito (Rp 50.000)")
            minum = input("Pilih minuman: ")
            if minum == "1":
                transaksi.tambahkan_barang(Minuman("Es Teh", 8000, True))
            elif minum == "2":
                transaksi.tambahkan_barang(Minuman("Teh Hangat", 7000, False))
            elif minum == "3":
                transaksi.tambahkan_barang(Minuman("Mojito", 50000, True))
            else:
                print("Pilihan tidak valid!")
        elif pilihan == "3":
            transaksi.struk_harga()
        elif pilihan == "4":
            print("Terima kasih telah berbelanja, semoga harimu menyenangkan!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
p = Makanan("Pizza", 100000, True)
print(p.get_nama())  # Output: Pizza

p.set_nama("Pizza Spesial")
p.set_harga(150000)

print(p.get_nama())  # Output: Pizza Spesial
print(p.get_harga()) # Output: 150000

