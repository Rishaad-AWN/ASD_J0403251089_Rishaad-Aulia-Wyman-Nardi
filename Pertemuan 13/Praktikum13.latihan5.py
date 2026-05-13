# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Kasus 2: Jaringan Komputer
# Menentukan koneksi antar router dengan total biaya minimum
# menggunakan algoritma Prim.
# ==========================================================

import heapq

# Representasi weighted graph jaringan router
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

def prim(graph, start):
    visited = set([start])
    heap = []

    # Masukkan semua edge awal dari node start
    for neighbor, weight in graph[start].items():
        heapq.heappush(heap, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while heap:
        weight, u, v = heapq.heappop(heap)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Ekspansi ke tetangga node baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (w, v, neighbor))

    return mst, total_weight

# Jalankan Prim mulai dari RouterA
mst, total = prim(graph, 'RouterA')

print("MST Jaringan Komputer (Prim):")
for edge in mst:
    print(f"  {edge[0]} -- {edge[1]} : bobot = {edge[2]}")

print(f"\nTotal bobot minimum = {total}")

# ==========================================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 2 - Jaringan Komputer (koneksi antar router).
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Prim, cocok untuk graph yang dense (banyak koneksi).
#
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterA - RouterC (bobot 2)
#    RouterC - RouterD (bobot 1)
#    RouterA - RouterB (bobot 3)
#
# 4. Berapa total bobot MST?
#    Total = 2 + 1 + 3 = 6
#
# 5. Mengapa edge tertentu tidak dipilih?
#    RouterB-RouterD (bobot 5) dan RouterB-RouterC (bobot 4)
#    tidak dipilih karena ketika giliran mereka dievaluasi,
#    semua node tujuannya sudah masuk ke dalam tree.
#    Menambahkannya akan membentuk cycle.
# ==========================================================
