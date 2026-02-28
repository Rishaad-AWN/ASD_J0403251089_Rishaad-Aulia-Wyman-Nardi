#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# Materi 6.3 - Rekursi pada Data List
# ==========================================================

def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list, kembalikan 0
    # Artinya tidak ada elemen lagi yang perlu dijumlahkan
    if index == len(data):
        return 0

    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    # Contoh: data=[2,4,6,8], index=0
    #   data[0] + jumlah_list(data, 1)
    #   2 + (4 + (6 + (8 + 0)))  = 20
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2, 4, 6, 8]))  # Output: 20
