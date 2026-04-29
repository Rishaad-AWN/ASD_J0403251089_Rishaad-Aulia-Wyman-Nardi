#===========================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#===========================================================
# Implementasi DFS
#===========================================================
from collections import deque

graph = {
  "A" : ["B", "C"],
  "B" : ["D", "E"],
  "C" : ["F", "G"],
  "D" : [],
  "E" : [],
  "F" : [],
  "G" : []
}

def dfs(graph, node, visited):
    # fungsi untuk melakukan penelusuran graph menggunakan DFS
    # graph : dictionary yang menyimpan graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    # tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Contoh data graph agar kode bisa berjalan
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# set visited
visited = set()

# Menjalankan dfs dari A
dfs(graph, "A", visited)