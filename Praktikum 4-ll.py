#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Implementasi Dasar : Node Pada Linked List
#======================================================

# Membuat class Node (merupakan unit dasar)
class Node:
  def __init__(self, data): # Konstruktor
    self.data = data # Menyimpan nilai / data
    self.next = None # Pointer ke Node berikutnya
    
# 1) Membuat Node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan Node Pertama (head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai None
current = head
while current is not None:
  print(current.data)
  current = current.next

#======================================================
# Implementasi Dasar : Linked List + Insert Awal
#======================================================

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_awal(self, data):
    # 1) Buat Node Baru
    nodeBaru = Node(data) # Panggil class Node
    
    # 2) Node menujuk ke head lama
    nodeBaru.next = self.head
    
    # 3) Head pindah ke Node baru
    self.head = nodeBaru
  
  def hapus_awal(self):
    data_terhapus = self.head.data
    # Menggeser head ke Node berikutnya
    self.head = self.head.next
    print(f"Data yang dihapus adalah : {data_terhapus}")
    
  def tampilkan(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next

print("\n")
print("=================== LIST BARU ===================")
ll = LinkedList() # Instantiasi objek ke class LinkedList
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
















