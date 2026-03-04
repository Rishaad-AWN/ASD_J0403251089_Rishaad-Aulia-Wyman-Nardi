# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

def insertion_sort(data):
 for i in range(1, len(data)):
  key = data[i]
  j = i - 1

 while j >= 0 and data[j] > key:
  data[j + 1] = data[j]
  j -= 1

 data[j + 1] = key

 return data

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?
'''

'''
Jawaban :
1. Karena elemen pertama (indeks 0) dianggap sudah terurut.
2. Menyimpan nilai yang akan dibandingkan dan disisipkan ke posisi yang tepat dalam bagian list yang sudah terurut.
3. Karena jumlah pergeseran tidak pasti.
while digunakan untuk terus menggeser elemen selama kondisi masih terpenuhi (data[j] > key).
4. Membandingkan elemen, Menggeser elemen ke kanan (data[j + 1] = data[j]) dan Mengurangi indeks j 
'''