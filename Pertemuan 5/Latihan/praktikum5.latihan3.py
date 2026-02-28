# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# Tujuan: Mengolah struktur data menggunakan rekursi
# ==========================================================

def cari_maks(data, index=0):
    # Base case: jika index sudah di elemen terakhir, kembalikan elemen itu
    # Tidak ada lagi elemen yang perlu dibandingkan
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari nilai maks dari sisa list (index berikutnya)
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan maks dari sisa list
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# ----------------------------------------------------------
# Diskusi:
# - Base case: index == len(data)-1, kembalikan elemen terakhir
# - Recursive case: bandingkan data[index] dengan hasil rekursi sisa list
# - Alur: cari_maks([3,7,2,9,5], 0)
#     -> maks_sisa = cari_maks([3,7,2,9,5], 1)
#         -> maks_sisa = cari_maks([3,7,2,9,5], 2)
#             -> maks_sisa = cari_maks([3,7,2,9,5], 3)
#                 -> maks_sisa = cari_maks([3,7,2,9,5], 4) = 5 (base case)
#                 -> 9 > 5? Ya -> return 9
#             -> 2 > 9? Tidak -> return 9
#         -> 7 > 9? Tidak -> return 9
#     -> 3 > 9? Tidak -> return 9
# - Hasil akhir: 9
# ----------------------------------------------------------
