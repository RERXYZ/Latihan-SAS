# Andreas Tegar Bagaskoro
# 102022500150
# S1 Sistem Informasi

def count_even(angka):
    count = 0
    for n in angka:
        if n % 2 == 0:
            count += 1
    return f"Jumlah bilangan genap: {count}"

print(count_even([1, 2, 3, 4, 5, 6]))
print(count_even([7, 9, 11])) #ganjil semua


#keterangan
# n % 2 = % -> modulus, berapa sisa pembagian n dengan 2?
# Kalau sisanya 0, berarti angkanya genap.
# 4 % 2 = 0 → genap
# 9 % 2 = 1 → ganjil