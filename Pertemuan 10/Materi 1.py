#===========================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#===========================================================

# ==========================================================
# MATERI 6.1 — KONSEP BST
# Aturan: semua nilai kiri < root < semua nilai kanan
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==========================================================
# MATERI 6.2 — INSERT BST
# data < node -> kiri | data > node -> kanan
# ==========================================================

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


# ==========================================================
# MATERI 6.3 — SEARCH BST
# key == root -> ketemu | key < root -> kiri | key > root -> kanan
# ==========================================================

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# ==========================================================
# MATERI — TRAVERSAL
# Inorder   (kiri->root->kanan) -> hasil selalu urut naik
# Preorder  (root->kiri->kanan) -> untuk melihat struktur tree
# Postorder (kiri->kanan->root) -> untuk menghapus tree
# ==========================================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# ==========================================================
# MATERI 6.4 — KELEMAHAN BST
# Data berurutan -> tree miring seperti Linked List -> O(n)
# Solusi: gunakan AVL Tree
# ==========================================================


# ==========================================================
# MATERI 6.5 — AVL NODE
# Sama seperti BST tapi ada atribut height
# ==========================================================

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1     # tambahan dibanding BST biasa


# ==========================================================
# MATERI 6.6 — BALANCE FACTOR
# BF = tinggi kiri - tinggi kanan
# BF -1/0/1 -> seimbang | BF >1 atau <-1 -> tidak seimbang
# ==========================================================

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


# ==========================================================
# MATERI 6.7 — ROTASI AVL
# Rotasi Kanan (LL): tree berat kiri  -> BF > 1
# Rotasi Kiri  (RR): tree berat kanan -> BF < -1
# ==========================================================

def rotate_right(y):
    x  = y.left
    T2 = x.right
    x.right = y         # y turun jadi child kanan x
    y.left  = T2        # T2 jadi child kiri y
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x            # x jadi root baru

def rotate_left(x):
    y  = x.right
    T2 = y.left
    y.left  = x         # x turun jadi child kiri y
    x.right = T2        # T2 jadi child kanan x
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y            # y jadi root baru


# ==========================================================
# MATERI 6.8 — INSERT AVL
# 1. Insert seperti BST
# 2. Update height
# 3. Cek balance factor
# 4. Rotasi jika tidak seimbang (4 kasus: LL, RR, LR, RL)
# ==========================================================

def avl_insert(root, data):
    # Langkah 1: insert seperti BST
    if root is None:
        return AVLNode(data)
    if data < root.data:
        root.left = avl_insert(root.left, data)
    elif data > root.data:
        root.right = avl_insert(root.right, data)
    else:
        return root

    # Langkah 2: update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Langkah 3: cek balance factor
    bf = get_balance(root)

    # Langkah 4: rotasi jika tidak seimbang
    if bf > 1 and data < root.left.data:        # LL -> rotasi kanan
        return rotate_right(root)
    if bf < -1 and data > root.right.data:      # RR -> rotasi kiri
        return rotate_left(root)
    if bf > 1 and data > root.left.data:        # LR -> kiri dulu, kanan
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if bf < -1 and data < root.right.data:      # RL -> kanan dulu, kiri
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


# ==========================================================
# MATERI 6.9 — PERBANDINGAN BST vs AVL
# BST: bisa tidak seimbang -> O(n)
# AVL: selalu seimbang     -> O(log n)
# ==========================================================


# ==========================================================
# FUNGSI BANTU TAMPILAN
# ==========================================================

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")


# ==========================================================
# DEMO
# ==========================================================

if __name__ == "__main__":

    print("=" * 45)
    print("DEMO BST — Insert, Traversal, Search")
    print("=" * 45)
    root_bst = None
    for d in [50, 30, 70, 20, 40, 60, 80]:
        root_bst = insert(root_bst, d)

    tampil_struktur(root_bst)
    print("\nInorder   :", end=" "); inorder(root_bst);   print()
    print("Preorder  :", end=" "); preorder(root_bst);  print()
    print("Postorder :", end=" "); postorder(root_bst); print()
    print("\nSearch 40 :", "DITEMUKAN" if search(root_bst, 40) else "TIDAK DITEMUKAN")
    print("Search 99 :", "DITEMUKAN" if search(root_bst, 99) else "TIDAK DITEMUKAN")

    print("\n" + "=" * 45)
    print("DEMO BST Tidak Seimbang")
    print("=" * 45)
    root_skew = None
    for d in [10, 20, 30, 40]:
        root_skew = insert(root_skew, d)
    tampil_struktur(root_skew)

    print("\n" + "=" * 45)
    print("DEMO AVL Tree — Insert Otomatis Seimbang")
    print("=" * 45)
    root_avl = None
    for d in [10, 20, 30, 40, 50]:
        root_avl = avl_insert(root_avl, d)
        print(f"Insert {d}:"); tampil_struktur(root_avl, level=1); print()

    print("\n" + "=" * 45)
    print("DEMO Rotasi Kiri & Kanan")
    print("=" * 45)

    # Rotasi Kiri
    r = AVLNode(10); r.right = AVLNode(20); r.right.right = AVLNode(30)
    print("Sebelum rotasi kiri:"); tampil_struktur(r)
    r = rotate_left(r)
    print("Sesudah rotasi kiri:"); tampil_struktur(r)

    print()

    # Rotasi Kanan
    r2 = AVLNode(30); r2.left = AVLNode(20); r2.left.left = AVLNode(10)
    print("Sebelum rotasi kanan:"); tampil_struktur(r2)
    r2 = rotate_right(r2)
    print("Sesudah rotasi kanan:"); tampil_struktur(r2)