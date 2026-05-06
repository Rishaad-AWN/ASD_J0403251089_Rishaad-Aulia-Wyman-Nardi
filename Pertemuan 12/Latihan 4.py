# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang':       {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan':  {'Lab': 3},
    'Kantin':        {'Lab': 4, 'Aula': 7},
    'Lab':           {'Aula': 1},
    'Aula':          {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak yang ada sudah lebih kecil
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ============================================================
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Kantin, dengan jarak 2 menit (langsung dari Gerbang).
#
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Waktu tempuh terpendek ke Aula = 7 menit.
#    Jalurnya: Gerbang->Kantin->Lab->Aula = 2+4+1 = 7 menit.
#    (Lebih cepat dari Gerbang->Kantin->Aula = 2+7 = 9 menit, atau
#     Gerbang->Perpustakaan->Lab->Aula = 6+3+1 = 10 menit)
#
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Tidak selalu. Contohnya, jalur dari Gerbang ke Aula secara langsung melalui
#    Kantin membutuhkan 2+7 = 9 menit, padahal melalui Lab bisa hanya 2+4+1 = 7 menit.
#    Jalur dengan lebih banyak singgahan bisa lebih cepat jika bobot edge-nya lebih kecil.
#
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Karena semua bobot (waktu tempuh) bernilai positif. Dijkstra dirancang
#    khusus untuk graph dengan bobot positif dan bekerja efisien menggunakan
#    priority queue, sehingga cocok untuk kasus navigasi lokasi seperti ini.
# ============================================================
