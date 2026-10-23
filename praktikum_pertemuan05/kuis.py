def tampilkan_soal(nomor, teks_soal):
    print(f"Soal {nomor}")
    print(teks_soal)
    print("pilih jawabanA, B, C, D")

def periksa_jawaban(jawaban_mahasiswa, kunci_jawaban):
    if jawaban_mahasiswa == kunci_jawaban:
        return True
    else:
        return False

def hitung_skor(jumlah_benar, jumlah_soal):
    skor = (jumlah_benar / jumlah_soal) * 100
    return skor

def main():
    soal = 1
    tampilkan_soal(soal, "Apa ibu kota Indonesia? A. Surabaya B. Bandung C. Medan D. Jakarta")
    jawaban = input("Jakarta: ")
    hasil = periksa_jawaban(jawaban, "D")
    if hasil:
        jumlah_benar = 1
    else:
        jumlah_benar = 0
    skor_akhir = hitung_skor(jumlah_benar, 1)
    print(f"skor akhir anda adalah: {skor_akhir}")
main()