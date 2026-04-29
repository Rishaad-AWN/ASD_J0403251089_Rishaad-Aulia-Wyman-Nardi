# Implementasi Dasar Graph

graph = {
  "A" : ["B", "C"],
  "B" : ["A", "D"],
  "C" : ["A", "D"],
  "D" : ["B", "C"]
}

# periksa semua node yang ada di dalam graph
for node in graph:
    # tampilkan node saat ini
    print("Node", node, "terhubung dengan tetangga:", end=" ")
    
    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # tampilkan tetangga tersebut
        print(neighbor, end=" ")
    
    # buat baris baru untuk node berikutnya
    print()