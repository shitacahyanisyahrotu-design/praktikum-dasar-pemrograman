harga_satuan = float(input("Masukan harga satuan:"))
jumlah = int(input("Masukan jumlah barang:"))
persen_diskon = float(input("Masukan persen diskon:"))

subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * (persen_diskon / 100)
total_bayar = subtotal - nominal_diskon

print("Subtotal = ", subtotal)
print("Nominal diskon = ", nominal_diskon)
print("Total = ", total_bayar)