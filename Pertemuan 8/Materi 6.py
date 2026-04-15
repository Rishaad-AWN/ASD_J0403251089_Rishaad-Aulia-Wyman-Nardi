#=====================================================================
# Nama : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
#=====================================================================

#=====================================================================
# Materi 5 : Struktur Organisasi Perusahaan
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data    # Menyimpan nilai pada node
    self.left = None    # Menyimpan referensi ke child kiri
    self.right = None   # Menyimpan referensi ke child kanan

def preorder(node):
  if node is not None:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

# Membuat tree struktur organisasi perusahaan
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")
root.right.right = Node("Staff 4")

# Menjalankan traversal postorder
print("Hasil Traversal Preorder : ", end="")
preorder(root)

# Penjelasan singkat:
# Kode ini merepresentasikan struktur organisasi perusahaan dalam bentuk binary tree.
# Root adalah "Direktur", lalu memiliki dua child yaitu "Manajer A" dan "Manajer B".
# Setiap manajer memiliki dua staff sebagai child.
# Fungsi preorder menampilkan urutan: root -> kiri -> kanan.
