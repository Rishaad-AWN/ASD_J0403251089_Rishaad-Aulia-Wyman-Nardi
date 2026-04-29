#=====================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# LATIHAN 5: Rotasi Kiri (Left Rotation - Kasus RR)
# Digunakan saat tree berat ke kanan (balance factor < -1)
#
# Sebelum rotasi:    Sesudah rotasi:
#   10                    20
#    \                   /  \
#    20        ->       10    30
#     \
#     30
#=====================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    # Dipakai untuk verifikasi BST property setelah rotasi
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

def rotate_left(x):
    y  = x.right    # y = child kanan x, akan jadi root baru
    T2 = y.left     # simpan subtree kiri y sementara
    y.left  = x     # x turun jadi child kiri y
    x.right = T2    # T2 jadi child kanan x
    return y        # kembalikan y sebagai root baru

# -----------------------------
# Program Utama
# -----------------------------

# Buat tree tidak seimbang (condong kanan)
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("--- SEBELUM Rotasi Kiri ---")
print("Preorder :", end=" "); preorder(root); print()
print("Inorder  :", end=" "); inorder(root);  print()
print("Struktur :"); tampil_struktur(root)

root = rotate_left(root)    # lakukan rotasi kiri

print("\n--- SESUDAH Rotasi Kiri ---")
print("Preorder :", end=" "); preorder(root); print()
print("Inorder  :", end=" "); inorder(root);  print()
print("Struktur :"); tampil_struktur(root)

# Diskusi:
# Rotasi kiri mengangkat node 20 menjadi root baru.
# Node 10 turun ke kiri dan node 30 tetap di kanan.
# Tree menjadi seimbang setelah rotasi.
# BST property tetap terjaga, terbukti dari inorder
# sebelum dan sesudah rotasi yang sama: 10 20 30.
# Rotasi kiri dipakai di AVL Tree untuk kasus RR
# (tree berat ke kanan, balance factor < -1).