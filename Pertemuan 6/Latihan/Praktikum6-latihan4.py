# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)
  
'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?
'''

'''
Jawaban:
1. Base case adalah kondisi penghentian rekursi, yaitu if len(data) <= 1.
   Jika list hanya memiliki 0 atau 1 elemen, list tersebut sudah terurut
   dan langsung dikembalikan tanpa diproses lebih lanjut.

2. Fungsi memanggil dirinya sendiri (rekursi) karena menggunakan strategi
   Divide and Conquer: masalah besar dibagi menjadi sub-masalah yang lebih
   kecil dan diselesaikan dengan cara yang sama, hingga mencapai base case.

3. Fungsi merge() bertugas menggabungkan dua sub-list yang sudah terurut
   menjadi satu list yang juga terurut, dengan membandingkan elemen
   terdepan dari kedua sub-list satu per satu.
'''

data = [38, 27, 43, 3, 9, 82, 10]
print("Sebelum:", data)
print("Sesudah:", merge_sort(data))
  

