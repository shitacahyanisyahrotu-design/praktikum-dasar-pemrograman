# Program kalkulator sederhana
print("=== Kalkulator Sederhana ===")
angka1 = float(input("Masukan angka pertama: "))
operator = input("Masukan operator (+, -, *, /): ")
angka2 = float(input("Masukan angka angka kedua: "))

if operator == "+":
    hasil = angka + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil = "operator tidak dikenal"

print("Hasil:", hasil)