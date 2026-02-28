#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Contoh Rekursi 1: Faktorial
# Materi 6.1 - Konsep Dasar Rekursif
# ==========================================================

def faktorial(n):
    # Base case: berhenti ketika n = 0
    # Faktorial dari 0 adalah 1 (nilai pasti, tidak perlu rekursi lagi)
    if n == 0:
        return 1

    # Recursive case: masalah diperkecil menjadi faktorial(n-1)
    # Contoh: faktorial(5) = 5 * faktorial(4)
    #         faktorial(4) = 4 * faktorial(3)
    #         ... terus sampai faktorial(0) = 1
    return n * faktorial(n - 1)

print(faktorial(5))  # Output: 120
