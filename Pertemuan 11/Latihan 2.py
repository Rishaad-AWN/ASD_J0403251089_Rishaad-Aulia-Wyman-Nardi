# ==============================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
# ==============================================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()

print("DFS dari A:")
dfs(graph, 'A', visited)
print("\n")

# ==============================================================================
# JAWABAN
# ==============================================================================
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
#    Jawaban: Karena DFS diimplementasikan menggunakan rekursi (atau stack 
#    berprinsip LIFO). Saat memeriksa tetangga pertama, fungsi akan memanggil 
#    dirinya sendiri untuk menelusuri tetangga tersebut secara terus menerus 
#    sampai mentok (tidak ada tetangga lagi), baru kemudian kembali (backtrack) 
#    untuk memproses cabang yang lain.
#
# 2. Apa yang terjadi jika urutan neighbor diubah?
#    Jawaban: Jalur cabang yang ditelusuri pertama kali akan berubah. Contohnya 
#    jika 'A': ['C', 'B'], maka DFS akan menelusuri cabang 'C' sampai terdalam 
#    (F) terlebih dahulu, baru kemudian backtrack dan menelusuri cabang 'B' (D, E).
#
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
#    Jawaban: 
#    - Output BFS: A B C D E F (mengeksplorasi secara melebar/level demi level).
#    - Output DFS: A B D E C F (mengeksplorasi satu jalur cabang sampai habis
#      sebelum pindah ke cabang lain di sebelahnya).
# ==============================================================================