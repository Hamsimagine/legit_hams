from datetime import datetime

def hitung_masa_kerja(tanggal_masuk, tanggal_akhir):
    format_tanggal = "%d-%m-%Y"  # Format tanggal: hari-bulan-tahun
    masuk = datetime.strptime(tanggal_masuk, format_tanggal)
    akhir = datetime.strptime(tanggal_akhir, format_tanggal)
    selisih = akhir - masuk

    # Menghitung jumlah tahun, bulan, dan hari
    total_hari = selisih.days
    tahun = total_hari // 365
    bulan = (total_hari % 365) // 30
    hari = (total_hari % 365) % 30

    return tahun, bulan, hari

# Input dari pengguna
tanggal_masuk = input("Masukkan tanggal masuk kerja (dd-mm-yyyy): ")
tanggal_akhir = input("Masukkan tanggal akhir masa kerja (dd-mm-yyyy): ")

# Menghitung masa kerja
tahun, bulan, hari = hitung_masa_kerja(tanggal_masuk, tanggal_akhir)

# Menampilkan hasil
print(f"Masa kerja: {tahun} tahun, {bulan} bulan, {hari} hari")