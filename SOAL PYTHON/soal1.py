# Fungsi untuk memeriksa apakah sebuah angka positif, negatif, atau nol
def check_number(num):
    if num > 0:
        print("positif")
    elif num < 0:
        print("negatif")
    else:
        print("nol")

# Contoh  
check_number(10)
check_number(-5)
check_number(0)