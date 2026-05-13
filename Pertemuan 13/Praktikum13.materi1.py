# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge pada graph awal (termasuk edge yang membentuk cycle)
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (tidak ada cycle, semua node terhubung)
# Dipilih 3 edge untuk 4 node (jumlah node - 1 = 3)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph awal:")
for edge in edges:
    print(f"  {edge}")

print("\nContoh Spanning Tree yang valid:")
for edge in spanning_tree:
    print(f"  {edge}")

print(f"\nJumlah edge graph awal   = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")

# ==========================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle (contoh: A-C-D-A).
#    Spanning tree hanya memiliki 3 edge (n-1), menghubungkan semua node
#    tanpa membentuk cycle apapun.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur redundan antar node yang meningkatkan biaya
#    tanpa menambah konektivitas. Tujuan spanning tree adalah koneksi
#    efisien minimum, sehingga cycle harus dihilangkan.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk n node, dibutuhkan tepat n-1 edge agar semua node terhubung
#    tanpa cycle. Edge lebih dari n-1 pasti membentuk cycle.
# ==========================================================
