import tkinter as tk

jendela = tk.Tk()
jendela.title("Kalkulator")
jendela.geometry("320x420")
jendela.configure(bg="black")

tampilan = ""

def tekan(tombol):
    global tampilan
    tampilan += str(tombol)
    label_hasil.config(text=tampilan)

def hasil():
    global tampilan
    try:
        # Konversi tampilan ke format Python
        ekspresi = tampilan.replace("×", "*").replace(":", "/")
        ekspresi = ekspresi.replace(",", ".")
        
        hitung = str(eval(ekspresi)).replace(".", ",")
        label_hasil.config(text=hitung)
        tampilan = hitung
    except:
        label_hasil.config(text="Error")
        tampilan = ""

def ac():
    global tampilan
    tampilan = ""
    label_hasil.config(text="0")

def plus_minus():
    global tampilan
    if tampilan:
        if tampilan.startswith("-"):
            tampilan = tampilan[1:]
        else:
            tampilan = "-" + tampilan
        label_hasil.config(text=tampilan)

def persen():
    global tampilan
    try:
        if tampilan:
            ekspresi = tampilan.replace(",", ".").replace("×", "*").replace(":", "/")
            nilai = eval(ekspresi)
            nilai = nilai / 100
            tampilan = str(nilai).replace(".", ",")
            label_hasil.config(text=tampilan)
    except:
        label_hasil.config(text="Error")
        tampilan = ""

label_hasil = tk.Label(jendela, text="0", font=("Arial", 30),
                       bg="black", fg="white", anchor="e")
label_hasil.pack(fill="both", pady=10)

frame = tk.Frame(jendela, bg="black")
frame.pack()

tombol_list = [
    ("AC", ac), ("+/-", plus_minus), ("%", persen), (":", lambda: tekan(":")),
    ("7", lambda: tekan("7")), ("8", lambda: tekan("8")), ("9", lambda: tekan("9")), ("×", lambda: tekan("×")),
    ("4", lambda: tekan("4")), ("5", lambda: tekan("5")), ("6", lambda: tekan("6")), ("−", lambda: tekan("-")),
    ("1", lambda: tekan("1")), ("2", lambda: tekan("2")), ("3", lambda: tekan("3")), ("+", lambda: tekan("+")),
    ("0", lambda: tekan("0")), (",", lambda: tekan(",")), ("=", hasil)
]

baris = 0
kolom = 0

for teks, fungsi in tombol_list:
    if teks == "AC":
        warna = "gray"
    elif teks in ["+", "−", "×", ":", "="]:
        warna = "orange"
    else:
        warna = "#333333"

    tombol = tk.Button(frame, text=teks, width=8, height=3, bg=warna,
                       fg="white", command=fungsi)
    tombol.grid(row=baris, column=kolom, padx=3, pady=3)

    kolom += 1
    if kolom > 3:
        kolom = 0
        baris += 1

jendela.mainloop()