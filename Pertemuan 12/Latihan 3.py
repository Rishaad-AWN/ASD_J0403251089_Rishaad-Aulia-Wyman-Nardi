# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3: Implementasi Bellman-Ford

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ============================================================
# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung A ke B = 5
#
# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobot A->C->B = 4 + (-2) = 2
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A->C->B dengan total bobot 2, lebih kecil dari jalur langsung A->B = 5.
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford tidak langsung "mengunci" jarak suatu node seperti Dijkstra.
#    Algoritma ini melakukan relaksasi berulang pada semua edge sebanyak (V-1) kali,
#    sehingga pengaruh bobot negatif bisa terdeteksi dan jarak bisa diperbarui
#    di iterasi berikutnya.
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi adalah proses memeriksa apakah jarak menuju suatu node (neighbor)
#    bisa dipersingkat dengan melewati node lain. Jika distances[node] + weight
#    lebih kecil dari distances[neighbor] yang sudah tercatat, maka jarak
#    distances[neighbor] diperbarui dengan nilai yang lebih kecil tersebut.
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    - Bellman-Ford: bisa menangani bobot negatif, lebih lambat O(V*E),
#      menggunakan pendekatan relaksasi berulang pada semua edge.
#    - Dijkstra: tidak bisa menangani bobot negatif, lebih cepat O((V+E) log V),
#      menggunakan pendekatan greedy dengan priority queue.
# ============================================================
