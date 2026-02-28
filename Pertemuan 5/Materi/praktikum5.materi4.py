# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# Materi 6.4 - Konsep Dasar Backtracking
# ==========================================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    # Berarti satu kombinasi sudah lengkap
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: tambah '0'
    # Pilih angka 0, lanjutkan rekursi untuk posisi berikutnya
    biner(n, hasil + "0")

    # Choose + Explore: tambah '1'
    # Pilih angka 1, lanjutkan rekursi untuk posisi berikutnya
    biner(n, hasil + "1")

# Memanggil dengan n=3, menghasilkan 8 kombinasi (2^3): 000 sampai 111
biner(3)
