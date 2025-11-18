class BankAccount:
    def __init__(self,saldo):
         self._saldo = saldo
         def deposit(self, jumlah):
              
            self._saldo+=jumlah
            print(f"Saldo: {self._saldo}")