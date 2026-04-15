#=====================================================================
# Nama : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# Materi 3 : Membuat Traversal Preorder
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

# Fungsi preorder : root -> left -> right
def preorder(node):
  if node is not None:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

# Membuat tree

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal preorder
print("Hasil Traversal Preorder : ", end="")
preorder(root)

# Penjelasan singkat:
# Fungsi preorder melakukan traversal tree dengan urutan: root -> kiri -> kanan.
# Menggunakan rekursi untuk mengunjungi setiap node.
# Tree dibuat dengan root "A", lalu child "B", "C", "D", dan "E".
# Output menampilkan urutan kunjungan node secara preorder.
