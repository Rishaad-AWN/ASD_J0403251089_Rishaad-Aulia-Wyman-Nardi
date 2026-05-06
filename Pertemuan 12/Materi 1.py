# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Materi 1: Implementasi Algoritma Dijkstra

import heapq

# Representasi weighted graph menggunakan nested dictionary
# Format: {node: {tetangga: bobot}}
graph = {
    'A': {'B': 4, 'C': 2},  # A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},           # B terhubung ke D (bobot 5)
    'C': {'D': 1},           # C terhubung ke D (bobot 1)
    'D': {}                  # D tidak memiliki tetangga (node tujuan)
}

def dijkstra(graph, start):
    """
    Fungsi mencari jarak terpendek dari node start ke semua node lain.
    Menggunakan pendekatan greedy: selalu pilih node dengan jarak terkecil.
    Parameter:
        graph : dict - weighted graph dalam bentuk nested dictionary
        start : str  - node awal pencarian
    Return:
        distances : dict - jarak minimum dari start ke setiap node
    """
    # Inisialisasi semua jarak dengan tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue: menyimpan (jarak, node), diurutkan dari jarak terkecil
    pq = [(0, start)]

    while pq:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak alternatif melalui node saat ini
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, perbarui dan masukkan ke queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Jalankan Dijkstra mulai dari node A
hasil = dijkstra(graph, 'A')
print("=== Hasil Dijkstra dari node A ===")
print(hasil)
# Output: {'A': 0, 'B': 4, 'C': 2, 'D': 3}
# Penjelasan:
# - A ke A = 0 (node awal)
# - A ke B = 4 (langsung A->B)
# - A ke C = 2 (langsung A->C)
# - A ke D = 3 (melalui A->C->D = 2+1 = 3, lebih kecil dari A->B->D = 4+5 = 9)
