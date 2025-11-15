# fungsi untuk menghitung jumlah bilangan genap dalam sebuah list
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print("Jumlah bilangan genap:", count)

# Contoh 
count_even([1, 2, 3, 4, 5, 6])
count_even([7, 9, 11])
