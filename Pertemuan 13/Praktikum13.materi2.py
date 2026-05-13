# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Algoritma Prim membangun MST dari satu node awal,
# lalu secara bertahap memilih edge terkecil ke node
# yang belum dikunjungi.
# ==========================================================

import heapq

# Representasi graph dalam bentuk adjacency dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])    # Set node yang sudah dikunjungi
    edges = []                # Min-heap untuk menyimpan edge kandidat

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)  # Ambil edge dengan bobot terkecil

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan edge-edge baru dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Jalankan Prim mulai dari node 'A'
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Prim):")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print(f"Total bobot = {total}")
