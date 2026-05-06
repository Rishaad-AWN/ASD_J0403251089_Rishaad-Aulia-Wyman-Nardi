# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota

import heapq

# Representasi graph berbobot antar kota menggunakan nested dictionary
# Bobot merepresentasikan jarak (atau waktu tempuh) antar kota
graph = {
    'Bogor':   {'Jakarta': 5, 'Depok': 2},  # Bogor terhubung ke Jakarta dan Depok
    'Depok':   {'Jakarta': 2, 'Bandung': 6}, # Depok terhubung ke Jakarta dan Bandung
    'Jakarta': {'Bandung': 7},               # Jakarta terhubung ke Bandung
    'Bandung': {}                            # Bandung tidak memiliki tetangga (tujuan akhir)
}

def dijkstra(graph, start):
    """
    Mencari jarak terpendek dari node start ke semua node lain.
    Menggunakan priority queue agar selalu memproses node dengan jarak terkecil duluan.
    """
    # Inisialisasi semua jarak dengan tak hingga (belum terjangkau)
    distances = {node: float('inf') for node in graph}

    # Jarak dari kota asal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: (jarak, kota), diurutkan dari jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil kota dengan jarak sementara terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil sudah tidak relevan (ada yang lebih kecil), lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota tetangga
        for neighbor, weight in graph[current_node].items():
            # Hitung total jarak jika melewati kota saat ini
            distance = current_distance + weight

            # Jika lebih kecil dari jarak yang tercatat, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Node awal: Bogor
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# ============================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah 'Bogor'.
#
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Depok, dengan jarak 2 (langsung Bogor->Depok).
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Bandung, dengan jarak 8.
#    Jalur terpendek ke Bandung: Bogor->Depok->Bandung = 2+6 = 8.
#    (Lebih kecil dari Bogor->Jakarta->Bandung = 5+7 = 12, atau
#     Bogor->Depok->Jakarta->Bandung = 2+2+7 = 11)
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:
#    - Mulai dari Bogor dengan jarak 0, semua kota lain jaraknya tak hingga.
#    - Proses Bogor: update Depok=2, Jakarta=5. Masukkan ke priority queue.
#    - Ambil Depok (jarak 2, terkecil): update Jakarta=min(5, 2+2)=4, Bandung=8.
#    - Ambil Jakarta (jarak 4): update Bandung=min(8, 4+7)=8 (tidak berubah).
#    - Ambil Bandung (jarak 8): tidak ada tetangga, selesai.
#    - Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8.
# ============================================================
