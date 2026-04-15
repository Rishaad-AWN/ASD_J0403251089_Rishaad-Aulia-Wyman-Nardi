#=====================================================================
# Nama : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# Materi 1 : Membuat Node
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

root = Node("A")

print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left)
print("Data child kanan root : ", root.right)


# Penjelasan :
# Class Node digunakan untuk membuat satu node pada binary tree.
# Setiap node punya data, serta child kiri (left) dan kanan (right) yang awalnya None.
# root = Node("A") membuat node utama (root) dengan isi "A".
# Output menampilkan data root dan child kiri/kanan yang masih kosong (None)..
