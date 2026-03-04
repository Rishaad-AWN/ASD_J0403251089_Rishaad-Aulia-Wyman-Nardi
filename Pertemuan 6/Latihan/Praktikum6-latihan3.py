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
Soal – Tracing dengan data = [5, 2, 4, 6, 1, 3]:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?
'''

'''
Jawaban:
1. Setelah iterasi i = 1:
   key = 2, data[0]=5 > 2 → geser
   Hasil: [2, 5, 4, 6, 1, 3]

2. Setelah iterasi i = 3:
   - i=2: key=4, data[1]=5 > 4 → geser → [2, 4, 5, 6, 1, 3]
   - i=3: key=6, data[2]=5 < 6 → tidak ada pergeseran
   Hasil: [2, 4, 5, 6, 1, 3]

3. Pada iterasi i = 4:
   key = 1, dibandingkan dengan 6, 5, 4, 2 → semuanya > 1 → 4 kali pergeseran
   Hasil setelah i=4: [1, 2, 4, 5, 6, 3]
'''

# Program tracing
data = [5, 2, 4, 6, 1, 3]
print("Data awal:", data)

for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    geser = 0
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
        geser += 1
    data[j + 1] = key
    print(f"Iterasi i={i}: {data}  | key={key}, pergeseran={geser}")