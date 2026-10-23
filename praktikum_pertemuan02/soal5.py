total_detik = int(input("Masukan total detik:"))

jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("Hasil konversi: {} jam, {} menit, {} detik".format(jam, menit, detik))