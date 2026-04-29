# ==============================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
# ==============================================================================

from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')
print("\n")

# ==============================================================================
# JAWABAN
# ==============================================================================
# 1. Node mana yang dikunjungi pertama?
#    Jawaban: Node 'Rumah', karena node tersebut ditetapkan sebagai node awal 
#    (start) yang dimasukkan pertama kali ke dalam queue.
#
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
#    Jawaban: Karena algoritma BFS menelusuri graph secara melebar level per 
#    level (menggunakan prinsip antrian FIFO). Dengan begitu, ia akan 
#    menemukan node terdekat (dengan jumlah edge paling sedikit dari titik 
#    awal) terlebih dahulu sebelum menjelajahi jalur yang lebih jauh.
#
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
#    Jawaban: Urutannya akan mengikuti struktur tetangga yang baru. Jika
#    tetangga sebuah node diubah urutannya, antrian (queue) akan memproses 
#    elemen sesuai urutan iterasi list baru tersebut. Namun, prinsip 
#    penelusuran per-level tetap sama (semua tetangga terdekat dieksplor 
#    dulu sebelum pindah ke tetangganya tetangga).
# ==============================================================================