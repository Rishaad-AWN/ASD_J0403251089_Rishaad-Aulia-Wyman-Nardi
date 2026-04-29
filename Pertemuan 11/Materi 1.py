#===========================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#===========================================================
# Implementasi Dasar Graph
#===========================================================

graph = {
  "A" : ["B", "C"],
  "B" : ["A", "D"],
  "C" : ["A", "D"],
  "D" : ["B", "C"]
}

# Mengambil setiap key dalam dictionary (mengunjungi semua node satu per satu)
for node in graph:
    # Menampilkan node dan daftar tetangganya (value)
    print(node, "->", graph[node])