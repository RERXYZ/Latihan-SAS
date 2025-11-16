a = float(input("Masukkan angka pertama: "))
op = input("Masukkan operator (+ - * /): ")
b = float(input("Masukkan angka kedua: "))

if op == "+":
    print("Hasil:", a + b)
elif op == "-":
    print("Hasil:", a - b)
elif op == "*":
    print("Hasil:", a * b)
elif op == "/":
    print("Hasil:", a / b)
else:
    print("Operator tidak valid")
