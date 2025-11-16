def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    print("Jumlah bilangan genap:", count)
