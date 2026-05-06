# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 1: Weighted Graph dan Perhitungan Jalur

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ============================================================
# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot A->B->D = 4 + 5 = 9
#
# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot A->C->D = 2 + 1 = 3
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur A -> C -> D dengan total bobot 3 dipilih sebagai jalur terpendek.
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena pada weighted graph, yang menjadi penentu bukan jumlah edge,
#    melainkan total bobot dari seluruh edge yang dilalui. Kedua jalur di atas
#    sama-sama melewati 2 edge, namun jalur A->C->D memiliki total bobot yang
#    jauh lebih kecil (3 vs 9). Dalam kasus lain, jalur dengan 3 edge bisa saja
#    lebih pendek dari jalur dengan 1 edge jika bobot totalnya lebih kecil.
# ============================================================
