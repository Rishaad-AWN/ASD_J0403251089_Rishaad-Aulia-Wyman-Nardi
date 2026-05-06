# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Materi 2: Implementasi Algoritma Bellman-Ford

# Weighted graph dengan bobot negatif (Dijkstra tidak bisa menangani ini)
# A->B=5, A->C=4, C->B=-2
graph = {
    'A': {'B': 5, 'C': 4},  # A ke B bobot 5, A ke C bobot 4
    'B': {},                  # B tidak punya tetangga
    'C': {'B': -2}            # C ke B dengan bobot negatif -2
}

def bellman_ford(graph, start):
    """
    Fungsi mencari jarak terpendek menggunakan algoritma Bellman-Ford.
    Berbeda dengan Dijkstra, Bellman-Ford mampu menangani bobot negatif.
    Cara kerja: melakukan relaksasi seluruh edge sebanyak (jumlah node - 1) kali.
    Parameter:
        graph : dict - weighted graph dalam bentuk nested dictionary
        start : str  - node awal pencarian
    Return:
        distances : dict - jarak minimum dari start ke setiap node
    """
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Relaksasi dilakukan sebanyak (jumlah node - 1) kali
    # Ini memastikan semua kemungkinan jalur terpendek ditemukan
    for _ in range(len(graph) - 1):
        # Periksa setiap edge dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Relaksasi: jika jarak melalui node ini lebih kecil, perbarui
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# Jalankan Bellman-Ford mulai dari node A
hasil = bellman_ford(graph, 'A')
print("=== Hasil Bellman-Ford dari node A ===")
for node, jarak in hasil.items():
    print(f"A -> {node} = {jarak}")

# Penjelasan hasil:
# - A ke A = 0
# - A ke C = 4 (langsung)
# - A ke B = 2 (melalui A->C->B = 4 + (-2) = 2, lebih kecil dari langsung A->B = 5)
# Bellman-Ford berhasil menemukan jalur terpendek meskipun ada bobot negatif
