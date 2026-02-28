# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# Materi 6.2 - Tracing Rekursi (Call Stack)
# ==========================================================

def hitung(n):
    # Base case: jika n = 0, fungsi berhenti dan tidak memanggil dirinya lagi
    if n == 0:
        print("Selesai")
        return

    print("Masuk:", n)   # fase stacking  - dicetak saat fungsi dipanggil masuk
    hitung(n - 1)         # pemanggilan rekursif - memanggil diri sendiri dengan n lebih kecil
    print("Keluar:", n)  # fase unwinding - dicetak saat fungsi kembali setelah rekursi selesai

# Memanggil fungsi dengan n=3
# Alur: hitung(3) -> hitung(2) -> hitung(1) -> hitung(0) -> balik satu per satu
hitung(3)
