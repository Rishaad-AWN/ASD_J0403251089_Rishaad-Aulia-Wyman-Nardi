#=====================================================================
# Materi 5 : Membuat Traversal Postorder
#=====================================================================

class Node:
  def __init__(self,data):
    self.data = data    # Menyimpan nilai pada node
    self.left = None    # Menyimpan referensi ke child kiri
    self.right = None   # Menyimpan referensi ke child kanan

def postorder(node):
  if node is not None:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")
    

# Membuat tree

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal postorder
print("Hasil Traversal Postorder : ", end="")
postorder(root)
