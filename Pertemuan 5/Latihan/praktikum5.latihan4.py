#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# Tujuan: Memahami pola choose dan explore
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case: jika panjang hasil sudah n, cetak dan kembali
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: pilih huruf 'A', lanjut ke posisi berikutnya
    kombinasi(n, hasil + "A")

    # Choose + Explore: pilih huruf 'B', lanjut ke posisi berikutnya
    kombinasi(n, hasil + "B")

# Memanggil dengan n=2
kombinasi(2)

# ----------------------------------------------------------
# Diskusi: Berapa jumlah kombinasi yang dihasilkan?
#
# Setiap posisi memiliki 2 pilihan (A atau B).
# Dengan n posisi, jumlah kombinasi = 2^n
# Untuk n=2: 2^2 = 4 kombinasi
# Hasilnya: AA, AB, BA, BB
#
# Jika n=3 maka hasilnya 2^3 = 8 kombinasi
# Pohon keputusan: setiap node bercabang dua (A dan B)
# sampai panjang string mencapai n (base case)
# ----------------------------------------------------------
