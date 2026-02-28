#========IDENTITAS MAHASISWA===================
#NAMA : _________________________________
#NIM  : ___________________________________
#Kelas: ______ / P1/P2
#================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# Materi 6.5 - Backtracking dengan Pruning (Pemangkasan)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    # Cabang ini tidak perlu dieksplorasi lagi karena pasti tidak memenuhi syarat
    if jumlah_1 > batas:
        return

    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Pilih '0' - jumlah_1 tidak bertambah
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' - jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Memanggil dengan n=4, batas maksimal '1' sebanyak 2
# Hanya kombinasi dengan jumlah angka 1 <= 2 yang akan dicetak
biner_batas(4, 2)
