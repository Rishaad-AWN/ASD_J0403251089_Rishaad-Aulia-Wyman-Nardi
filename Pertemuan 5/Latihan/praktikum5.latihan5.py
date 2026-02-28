# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ==========================================================
# Studi Kasus: Generator PIN
# Tujuan: Membuat semua kemungkinan PIN 3 digit (angka 0-2)
#         menggunakan teknik backtracking
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Base case: jika panjang string hasil sudah sesuai, cetak PIN
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Loop untuk setiap angka yang tersedia (0, 1, 2)
    # Setiap iterasi: pilih angka, tambahkan ke hasil, lanjut rekursi
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)  # explore ke posisi berikutnya

# Memanggil untuk membuat PIN 3 digit
# Total kombinasi: 3^3 = 27 PIN
buat_pin(3)

# ----------------------------------------------------------
# Diskusi: Bagaimana cara mencegah angka yang sama muncul berulang?
#
# Saat ini angka boleh muncul berulang (misal: 000, 111, 222).
# Untuk mencegah angka yang sama muncul berulang dalam satu PIN,
# kita bisa menambahkan pengecekan: angka yang dipilih tidak boleh
# sudah ada di dalam string 'hasil'.
#
# Contoh modifikasi:
#   for angka in ["0", "1", "2"]:
#       if angka not in hasil:   <-- tambahkan kondisi ini
#           buat_pin(panjang, hasil + angka)
#
# Dengan cara ini, setiap angka hanya boleh muncul sekali per PIN,
# sehingga kombinasi seperti 000 atau 112 tidak akan dicetak.
# ----------------------------------------------------------
