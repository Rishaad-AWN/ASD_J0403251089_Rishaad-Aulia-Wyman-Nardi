# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
 print(edge)
print("\nSpanning Tree:")

for edge in spanning_tree:
 print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban : 
# 1. Perbedaan graph awal yaitu tidak membentuk edge yang cycle dan graph tree membentuk graph cycle
# 2. Spanning tree tidak boleh memiliki cycle karena definisi dasar dari sebuah tree dalam teori graf adalah graf terhubung yang tidak mengandung sirkuit atau cycle.
# 3. Karena langkah pertama dari spanning tree adalah urutkan seluruh edge berdasarkan bobot terkecil. 