#=====================================================================
# Nama : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# Materi 2 : Membuat child pada Node
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

root = Node("A")


# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
# Menampilkan isi Node

print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left)
print("Data child kanan root : ", root.right)
print("Data child kiri B : ", root.left.left)
print("Data child kanan C : ", root.left.right)

# Penjelasan :
# Kode ini membuat binary tree dengan menambahkan child ke node.
# root = "A", lalu ditambahkan child kiri "B" dan kanan "C" (level 1).
# Node "B" memiliki child "D" (kiri) dan "E" (kanan) di level 2.
# Output menampilkan data root dan beberapa child (masih berupa objek node, bukan isi datanya).