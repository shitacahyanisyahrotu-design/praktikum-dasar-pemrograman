soal = [
    "makana khas brebes?",
    "3 + 5 + 2 hasilnya adalah?",
    "smaga catnya?",
    "berapa umur shita?",
    "berapa provinsi di indonesia?",
]

kunci = ["telor asin", "10", "ijo", "18", "38"]
skor = 0

for nomor in range(len(soal)):
    print(f"\nsoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("jawaban anda: ")

    if jawaban.strip().lower() == kunci[nomor].lower():
        print("benar!")
        skor += 10
    else:
        print(f"salah. jawaban benar: {kunci[nomor]}")

print(f"\nskor akhir anda: {skor}/{len(soal)}")