#=====================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# LATIHAN 4: BST Tidak Seimbang
# Jika data dimasukkan berurutan naik, setiap nilai baru
# selalu lebih besar dari node sebelumnya sehingga selalu
# masuk ke kanan -> tree condong kanan (right-skewed)
#=====================================================================

class Node:
    def __init__(self, data):
        self.data = data    # nilai pada node
        self.left = None    # child kiri
        self.right = None   # child kanan

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def preorder(root):
    # Urutan: root -> kiri -> kanan
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    # Tampilkan tree dengan indentasi per level
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

def hitung_tinggi(root):
    if root is None:
        return 0
    return 1 + max(hitung_tinggi(root.left), hitung_tinggi(root.right))

def balance_factor(node):
    # BF = tinggi kiri - tinggi kanan
    # -1, 0, 1 = seimbang | >1 atau <-1 = tidak seimbang
    if node is None:
        return 0
    return hitung_tinggi(node.left) - hitung_tinggi(node.right)

# -----------------------------
# Program Utama
# -----------------------------
root = None
data_list = [10, 20, 30]   # data berurutan -> penyebab tidak seimbang
for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)
print("\n\nStruktur BST:")
tampil_struktur(root)
print(f"\nTinggi tree         : {hitung_tinggi(root)}")
print(f"Balance factor root : {balance_factor(root)}")

# Diskusi:
# Tree condong ke kanan karena data [10, 20, 30] dimasukkan
# secara berurutan naik, setiap nilai selalu masuk ke kanan.
# Balance factor root = -2, artinya tidak seimbang
# (nilai valid hanya -1, 0, atau 1).
# Akibatnya pencarian jadi O(n) seperti Linked List,
# bukan O(log n) seperti BST yang seimbang.
# Untuk mengatasi ini digunakan AVL Tree yang otomatis
# melakukan rotasi saat tree tidak seimbang.