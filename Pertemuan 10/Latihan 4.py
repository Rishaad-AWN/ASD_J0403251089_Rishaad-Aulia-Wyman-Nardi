#=====================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#=====================================================================


#=====================================================================
# LATIHAN 6: Rotasi Kanan (Right Rotation - Kasus LL)
# Digunakan saat tree berat ke kiri (balance factor > 1)
#
# Sebelum rotasi:    Sesudah rotasi:
#     30                  20
#    /                   /  \
#   20        ->        10    30
#  /
# 10
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

def rotate_right(y):
    x  = y.left     # x = child kiri y, akan jadi root baru
    T2 = x.right    # simpan subtree kanan x sementara
    x.right = y     # y turun jadi child kanan x
    y.left  = T2    # T2 jadi child kiri y
    return x        # kembalikan x sebagai root baru

# -----------------------------
# Program Utama
# -----------------------------

# Buat tree tidak seimbang (condong kiri)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("--- SEBELUM Rotasi Kanan ---")
print("Preorder :", end=" "); preorder(root); print()
print("Inorder  :", end=" "); inorder(root);  print()
print("Struktur :"); tampil_struktur(root)

root = rotate_right(root)   # lakukan rotasi kanan

print("\n--- SESUDAH Rotasi Kanan ---")
print("Preorder :", end=" "); preorder(root); print()
print("Inorder  :", end=" "); inorder(root);  print()
print("Struktur :"); tampil_struktur(root)

# Diskusi:
# Rotasi kanan adalah kebalikan dari rotasi kiri.
# Node 20 naik jadi root baru, node 30 turun ke kanan,
# node 10 tetap di kiri. Tree menjadi seimbang.
# BST property tetap terjaga, terbukti dari inorder
# sebelum dan sesudah rotasi yang sama: 10 20 30.
# Rotasi kanan dipakai di AVL Tree untuk kasus LL
# (tree berat ke kiri, balance factor > 1).