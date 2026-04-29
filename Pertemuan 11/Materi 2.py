from collections import deque
# Implementasi BFS

graph = {
  "A" : ["B", "C"],
  "B" : ["D", "E"],
  "C" : ["F", "G"],
  "D" : [],
  "E" : [],
  "F" : [],
  "G" : []
}

def bfs(graph, start):
  # Fungsi untuk melakukan penelusuran graph dengan BFS
  # graph : dictionary yang menyimpan struktur dari graph
  # start : node awal penelusuran
  
  # Queue digunakan untuk menyimpan node yang akan diproses / dibaca
  queue = deque()
  
  # Variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
  visited = set()
  
  # Masukkan node awal ke queue
  queue.append(start)
  
  # tandai node awal sebagai node yang sudah dikunjungi
  visited.add(start)
  
  while queue:
      # mengambil node paling depan dari queue
      node = queue.popleft()
      print(node, end=" ")
  
      # periksa semua tetangga dari node yang diambil
      for neighbor in graph[node]:
          if neighbor not in visited:
              visited.add(neighbor)
              queue.append(neighbor)

# Menjalankan BFS mulai dari node "A"
bfs(graph, "A")