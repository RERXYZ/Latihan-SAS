def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(f"Jumlah bilangan genap: {count}")


# contoh pemanggilan
count_even([1, 2, 3, 4, 5, 6])   
count_even([7, 9, 11])           
