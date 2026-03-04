# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().
'''

# Jawaban

# No. 1
def merge_lengkap(left, right):
    result = []
    i = 0
    j = 0
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
    left_sorted = merge_sort(data[:mid])
    right_sorted = merge_sort(data[mid:])
    return merge_lengkap(left_sorted, right_sorted)
  
# No. 2

'''
result.extend(list) menambahkan semua elemen dari sebuah list ke dalam result satu per satu (berbeda dengan append yang menambahkan list sebagai satu elemen utuh).

Digunakan untuk menambahkan sisa elemen kiri atau kanan yang belum diproses setelah loop while selesai, karena sisa tersebut sudah pasti terurut dan lebih besar dari semua elemen yang sudah ada di result.
'''

data = [38, 27, 43, 3, 9, 82, 10]
print("Sebelum:", data)
print("Sesudah:", merge_sort(data))