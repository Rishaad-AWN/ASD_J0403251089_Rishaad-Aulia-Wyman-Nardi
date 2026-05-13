# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1 (bobot terkecil dari semua edge).
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Strategi greedy Kruskal selalu memilih edge terkecil agar total
#    bobot MST menjadi minimum.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 1 + 2 + 3 = 6
#    (edge C-D=1, A-C=2, B-D=3)
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#    saat giliran mereka, semua node sudah terhubung. Menambahkan
#    edge tersebut akan membentuk cycle.
# ==========================================================
