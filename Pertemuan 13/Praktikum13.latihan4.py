# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Kasus: Kampus ingin menghubungkan 4 gedung dengan kabel
# internet, menggunakan biaya pemasangan minimum.
# Algoritma yang digunakan: Kruskal
# ==========================================================

# Daftar edge: (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Urutkan berdasarkan biaya terkecil (strategi Kruskal)
edges.sort()

mst = []
total_cost = 0
connected = set()

for cost, u, v in edges:
    # Tambahkan edge jika tidak membentuk cycle
    if u not in connected or v not in connected:
        mst.append((u, v, cost))
        total_cost += cost
        connected.add(u)
        connected.add(v)

print("Jaringan Kabel Optimal (MST):")
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]} : biaya = {edge[2]}")

print(f"\nTotal biaya minimum pemasangan kabel = {total_cost}")

# ==========================================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Kruskal, karena datanya berupa daftar edge (sparse graph).
#
# 2. Edge mana saja yang dipilih?
#    GedungC - GedungD (biaya 1)
#    GedungA - GedungC (biaya 2)
#    GedungB - GedungD (biaya 3)
#
# 3. Berapa total biaya minimum?
#    Total = 1 + 2 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    MST menjamin semua gedung terhubung tanpa jalur redundan
#    (cycle) dengan total biaya kabel paling rendah. Jalur
#    redundan hanya memboroskan biaya tanpa manfaat konektivitas.
# ==========================================================
