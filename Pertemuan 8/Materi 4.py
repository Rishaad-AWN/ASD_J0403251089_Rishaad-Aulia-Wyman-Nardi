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
