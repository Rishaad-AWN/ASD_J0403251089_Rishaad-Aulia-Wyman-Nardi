# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending.
2. Ubah agar menjadi descending.
'''

# Jawaban

# 1. Ascending
def insertion_sort_asc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# 2. Descending
def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

data = [38, 27, 43, 3, 9, 82, 10]
print("Sebelum   :", data)
print("Ascending :", insertion_sort_asc(data.copy()))
print("Descending:", insertion_sort_desc(data.copy()))
