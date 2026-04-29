#=====================================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#=====================================================================

#=====================================================================
# LATIHAN 1: Node dan Insert BST
# BST = Binary Tree dengan aturan: kiri < root < kanan
# Setiap data baru dicari posisinya dengan rekursi
#=====================================================================

class Node:
    def __init__(self, data):
        self.data = data    # nilai yang disimpan di node
        self.left = None    # child kiri
        self.right = None   # child kanan

def insert(root, data):
    if root is None:
        return Node(data)           # posisi kosong -> buat node baru
    if data < root.data:
        root.left = insert(root.left, data)     # lebih kecil -> kiri
    elif data > root.data:
        root.right = insert(root.right, data)   # lebih besar -> kanan
    return root

# Membuat BST
root = None
data_list = [50, 30, 70, 20, 40, 60, 80]
for data in data_list:
    root = insert(root, data)

print("LATIHAN 1: BST berhasil dibuat")
print(f"Data: {data_list}")
# Hasil struktur tree:
#        50
#       /  \
#      30   70
#     / \  / \
#    20 40 60 80

# Diskusi:
# BST menyimpan data dengan aturan kiri < root < kanan di setiap node.
# Data 30 masuk kiri karena 30 < 50, data 70 masuk kanan karena 70 > 50.
# Fungsi insert bekerja secara rekursif sampai menemukan posisi kosong (None),
# lalu membuat node baru di posisi tersebut.


#=====================================================================
# LATIHAN 2: Traversal Inorder
# Urutan kunjungan: kiri -> root -> kanan
# Hasilnya selalu urut naik karena sifat BST
#=====================================================================

def inorder(root):
    if root is not None:
        inorder(root.left)              # kunjungi kiri dulu
        print(root.data, end=" ")       # cetak root
        inorder(root.right)             # lalu kanan

print("\nLATIHAN 2: Hasil inorder:")
inorder(root)
print()

# Diskusi:
# Inorder BST selalu menghasilkan data urut ascending.
# Ini karena semua node kiri < root < semua node kanan,
# sehingga saat dikunjungi kiri-root-kanan hasilnya terurut.
# Inorder bisa dipakai sebagai sorting otomatis.


#=====================================================================
# LATIHAN 3: Search BST
# Manfaatkan aturan BST untuk mempersingkat pencarian
# Tidak perlu cek semua node, cukup ikuti arah yang benar
#=====================================================================

def search(root, key):
    if root is None:
        return False                    # sampai ujung, tidak ditemukan
    if root.data == key:
        return True                     # ketemu
    elif key < root.data:
        return search(root.left, key)   # key lebih kecil -> cari kiri
    else:
        return search(root.right, key)  # key lebih besar -> cari kanan

print("\nLATIHAN 3: Hasil Search:")
for key in [40, 10, 70, 99]:
    hasil = "DITEMUKAN" if search(root, key) else "TIDAK DITEMUKAN"
    print(f"  Cari {key} -> {hasil}")

# Diskusi:
# Pencarian BST efisien karena setiap langkah membuang
# setengah bagian tree yang tidak mungkin berisi data.
# Kompleksitas O(log n) untuk tree seimbang,
# berbeda dengan array biasa yang O(n).