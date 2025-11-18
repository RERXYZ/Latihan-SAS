class buku:
    def __init__(self, judul, harga):
        self.judul=judul
        self.harga = harga
    def _str_(self):
        return f"{self.judul} - Rp {self.harga}"
    def _add_(self,other):
        return self.harga + other.harga
b1 = buku ("Naruto", 50000)
b2 = buku ("One piece", 60000)

print(b1)
print(b1+b2)