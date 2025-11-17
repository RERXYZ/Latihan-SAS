# penjelasan enkapsulasi dalam oop
# Menyembunyikan detail data atau fungsi agar tidak diakses langsung dari luar

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # atribut private

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Saldo tidak boleh negatif!")

    # Method publik
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Saldo kurang!")

# Contoh penggunaan
acc = BankAccount("Budi", 1000)

print(acc.get_balance())  # akses via getter

acc.deposit(500)
print(acc.get_balance())  # 1500

acc.set_balance(-100)     # akan ditolak