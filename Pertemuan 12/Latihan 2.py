# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 2: Implementasi Dijkstra

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati (node sudah diproses dengan jarak lebih kecil)
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ============================================================
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
#    Jarak A ke B = 4 (langsung melalui edge A->B)
#
# 2. Berapa jarak terpendek dari A ke C?
#    Jarak A ke C = 2 (langsung melalui edge A->C)
#
# 3. Berapa jarak terpendek dari A ke D?
#    Jarak A ke D = 3 (melalui jalur A->C->D = 2+1 = 3)
#
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Karena A->C->D = 2+1 = 3, sedangkan A->B->D = 4+5 = 9.
#    Meskipun jumlah edge sama (2 edge), total bobot jalur via C jauh lebih kecil.
#
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Priority queue memastikan node dengan jarak sementara terkecil selalu
#    diproses terlebih dahulu. Ini adalah kunci dari pendekatan greedy Dijkstra,
#    sehingga setiap kali kita memproses sebuah node, jarak ke node tersebut
#    sudah merupakan jarak minimum yang final.
#
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Dijkstra menggunakan asumsi greedy yang berarti sebuah node diproses,
#    jaraknya sudah final dan tidak bisa berubah. Jika ada bobot negatif,
#    asumsi ini bisa dilanggar karena jalur yang awalnya lebih panjang
#    bisa menjadi lebih pendek setelah melewati edge negatif, sehingga
#    algoritma bisa menghasilkan hasil yang salah.
# ============================================================
