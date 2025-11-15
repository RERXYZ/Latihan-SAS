# menu penjumlah, pengurangan, perkalian, dan pembagian 
def penjumlahan(x, y):
    return x + y
def pengurangan(x, y):
    return x - y
def perkalian(x, y):
    return x * y
def pembagian(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# fungsi utama
def calculator():
    print("\n\nPilih operation:")
    print("1. Penjumlahan ( + )")
    print("2. Pengurangan ( - )")
    print("3. Perkalian ( x )")
    print("4. Pembagian ( / )")
    while True:
        choice = input("\nPilih Menu Penjumlahan ( 1 / 2 / 3 / 4 ) : ")
        if choice in ['1', '2', '3', '4']:
            print("\n================================\n")
            num_count = int(input("Berapa banyak angka yang ingin Anda hitung? "))
            numbers = []
            for i in range(num_count):
                num = float(input(f"Masukkan angka ke-{i+1}: "))
                numbers.append(num)
            if choice == '1':
                result = sum(numbers)
                print("\nHasil penjumlahan:", result)
                print("\n================================\n")
            elif choice == '2':
                result = numbers[0]
                for num in numbers[1:]:
                    result = pengurangan(result, num)
                print("\nHasil pengurangan:", result)
                print("\n================================\n")
            elif choice == '3':
                result = 1
                for num in numbers:
                    result = perkalian(result, num)
                print("\nHasil perkalian:", result)
                print("\n================================\n")
            elif choice == '4':
                result = numbers[0]
                for num in numbers[1:]:
                    result = pembagian(result, num)
                print("\nHasil pembagian:", result)
                print("\n================================\n")
            break
        else:
            print("Invalid Input")

# main function
if __name__ == "__main__":
    calculator()