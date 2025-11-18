class buku:
    jenis ="komik"
    @classmethod
    def ubah_jenis(cls,jenis_baru):
        cls.jenis=jenis_baru
buku.ubah_jenis("Novel")
print(buku.jenis)
