#=====================================================================
# Nama : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# Materi 4 : Membuat Traversal Preorder
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data    # Menyimpan nilai pada node
    self.left = None    # Menyimpan referensi ke child kiri
    self.right = None   # Menyimpan referensi ke child kanan
# Membuat Fungsi : root -> left -> right
def inorder(node):
  if node is not None:
    inorder(node.left)
    print(node.data, end="")
    inorder(node.right)
# Membuat tree

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal inorder
print("Hasil Traversal Inorder : ", end="")
inorder(root)

# Penjelasan singkat:
# Fungsi inorder melakukan traversal dengan urutan: kiri -> root -> kanan.
# Menggunakan rekursi untuk mengunjungi node.
# Tree dibuat dengan root "A" dan beberapa child.
# Output menampilkan urutan node sesuai inorder.
