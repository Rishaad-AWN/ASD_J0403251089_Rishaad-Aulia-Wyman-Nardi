#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# Tujuan: Memahami base case dan recursive case
# ==========================================================

def pangkat(a, n):
    # Base case: berhenti ketika n = 0
    # Setiap bilangan yang dipangkatkan 0 hasilnya 1
    if n == 0:
        return 1

    # Recursive case: masalah diperkecil
    # pangkat(2, 4) = 2 * pangkat(2, 3)
    # pangkat(2, 3) = 2 * pangkat(2, 2)
    # pangkat(2, 2) = 2 * pangkat(2, 1)
    # pangkat(2, 1) = 2 * pangkat(2, 0)
    # pangkat(2, 0) = 1  <-- base case
    # Hasil akhir: 2*2*2*2*1 = 16
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))  # Output: 16

# ----------------------------------------------------------
# Diskusi:
# - Base case: n == 0, mengembalikan 1 agar rekursi berhenti
# - Recursive case: a * pangkat(a, n-1), setiap pemanggilan n berkurang 1
# - Alur call stack: pangkat(2,4) -> pangkat(2,3) -> pangkat(2,2)
#   -> pangkat(2,1) -> pangkat(2,0) -> mulai kembali (unwinding)
# ----------------------------------------------------------
