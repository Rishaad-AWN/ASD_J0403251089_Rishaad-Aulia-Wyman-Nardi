#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# Tujuan: Memahami alur masuk dan keluar fungsi
# ==========================================================

def countdown(n):
    # Base case: ketika n = 0, rekursi berhenti
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)   # dicetak saat masuk (fase stacking)
    countdown(n - 1)      # rekursi: panggil dengan n lebih kecil
    print("Keluar:", n)  # dicetak saat kembali (fase unwinding)

countdown(3)

# ----------------------------------------------------------
# Diskusi: Mengapa output 'Keluar' muncul terbalik?
#
# Karena print("Keluar:", n) berada SETELAH pemanggilan rekursif.
# Fungsi tidak akan mencetak "Keluar" sampai semua rekursi di bawahnya
# selesai dieksekusi terlebih dahulu.
#
# Urutan eksekusi:
#   countdown(3) -> Masuk: 3
#     countdown(2) -> Masuk: 2
#       countdown(1) -> Masuk: 1
#         countdown(0) -> Selesai (base case, langsung return)
#       kembali ke countdown(1) -> Keluar: 1
#     kembali ke countdown(2) -> Keluar: 2
#   kembali ke countdown(3) -> Keluar: 3
#
# Hasilnya "Keluar" muncul dari 1, 2, 3 (terbalik dari urutan masuk)
# karena sifat call stack: yang terakhir masuk, pertama keluar (LIFO)
# ----------------------------------------------------------
