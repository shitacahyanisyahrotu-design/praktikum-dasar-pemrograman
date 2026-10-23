def konversi_menit_ke_detik(menit):
    """
    Mengkonversi waktu dari menit ke detik.
    
    parameter :
        menit : Waktu dalam menit.
    
    Returns:
        Waktu dalam detik.
    """
    detik = menit * 60
    return detik

print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)