# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi graph sebagai adjacency dictionary (weighted)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])   # Mulai dari node awal
    edges = []

    # Masukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)  # Ambil edge terkecil

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Eksplorasi edge baru dari node yang baru ditambahkan
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node 'A' digunakan sebagai titik awal.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2 (edge terkecil dari node A).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Setelah node C ditambahkan, semua edge dari A dan C dimasukkan
#    ke heap. Edge terkecil berikutnya adalah C-D (bobot 1), lalu
#    D-B (bobot 3). Prim selalu memilih edge terkecil yang
#    menghubungkan node dalam tree ke node di luar tree.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total = 2 + 1 + 3 = 6
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal: memilih edge terkecil secara global dari seluruh daftar edge.
#    Prim: membangun tree dari satu node, ekspansi ke tetangga terdekat.
#    Keduanya menghasilkan MST yang sama (total bobot sama), hanya
#    urutan pemilihan edge yang berbeda.
# ==========================================================
