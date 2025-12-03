class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo      

    
    def lihat_saldo(self):
        return self.__saldo

  
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

   
    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup!")



akun = AkunBank("Budi", 500000)

print(akun.lihat_saldo())    

akun.setor(300000)
print(akun.lihat_saldo())

akun.tarik(200000)
print(akun.lihat_saldo())