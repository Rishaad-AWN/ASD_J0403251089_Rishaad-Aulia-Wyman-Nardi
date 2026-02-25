#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Implementasi Dasar : Node Pada Queue
#======================================================

class Node:
  def __init__(self, data): # Konstruktor
    self.data = data # Menyimpan nilai / data
    self.next = None # Pointer ke Node berikutnya

# Queue dengan 2 pointer : front dan rear

class QueueLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def is_empty(self):              
    return self.head is None
    
  def enqueue(self ,data):
    # Menambah data di belakang (rear)
    nodeBaru = Node(data)
    
    # Jika queue kosong, front dan rear menujuk ke node yang sama
    if self.is_empty():
      self.head = nodeBaru
      self.tail = nodeBaru
      return
    
    # Jika queue tidak kosong : 
    # Rear lama menujuk ke node baru
    self.tail.next = nodeBaru
    # Rear pindah ke node baru
    self.tail = nodeBaru
  
  def dequeue(self):
    
    # 1) Lihat data yang paling depan
    data_terhapus = self.head.data

    # 2) Geser front ke node berikutnya
    self.front = self.head.next
    
    # 3) Jika setelah geser front menjadi none, maka queue kosong
    # Rear juga harus jadi None
    if self.front is None:
      self.head = None
    return data_terhapus
    
  def tampilkan(self):
    # Menampilkan isi queue
    current = self.head
    print("Front ->", end="->")    
    while current is not None:
      print(current.data, end="->")
      current = current.next
    print("None - Rear di node terakhir")
    
# Instantiasi objek class QueueLinkedList
q = QueueLinkedList()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()

















    