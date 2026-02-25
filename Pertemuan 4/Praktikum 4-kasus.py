#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Studi Kaus : Sistem Antrian   Layanan Akademik
#Implementasi Queue =>
#Enqueue  : Memindahkan Pointer Rear (Nambahkan Data Baru Dari Belakang)
#Dequeue  : Memindahkan Pointer Front (Memindahkan Data Baru Dari Depan)
# Front-> ->Rear
#======================================================

#1) Mendefinisikan Node (Unit dasar linked list)

class Node:
  def __init__(self, data_nim, data_nama):
    self.nim = data_nim   # Menyimpan NIM Mahasiswa
    self.nama = data_nama   # Menyimpan Nama Mahasiswa
    self.next = None   # Pointer ke Node Berikutnya

# Mendefinisikan queue, terdiri dari head dan tail
class queue_Akademik:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def is_empty(self): 
    # Ketika Queue Kosong Maka Head = Tail = None             
    return self.head is None
  
  def enqueue(self, data_nim, data_nama):
    nodeBaru = Node(data_nim, data_nama)
    # Jika Data Baru Masuk dari Queue yang kosong maka data baru = head = tail
    if self.is_empty():
      self.head = nodeBaru
      self.tail = nodeBaru
      return
    
    # Jika queue tidak kosong, maka data baru diletakan setelah tail kemusian dijadikan sebagai tail
    self.tail.next = nodeBaru
    self.tail = nodeBaru
    
    
  # Menghapus data paling depan (Memberikan Layanan Akademik)
  def dequeue(self):
    
    if self.is_empty():
      print("Antrian kosong, Tidak ada mahasiswa dilayani")
      return None
    
    # Lihat data bagian head, simpan di variabel data yang akan dihapus (dilayani)
    node_dilayani = self.head
    
    # Geser pointer front ke selanjutnya
    self.head = self.head.next
    
    # Jika head menjadi none (data antrian terakhir yang dilayani), maka head = tail = none
    if self.head is None:
      self.tail = None
    
    return node_dilayani
  
  def tampilkan(self):
    if self.is_empty():
        print("Antrian kosong")
        return
      
    print("Daftar Antrian Mahasiswa (Head -> Tail) : ")
    current = self.head
    no = 1
    while current is not None:
      print(f"{no}. {current.nim} - {current.nama}")
      current = current.next
      no += 1
      
# Program Utama

def main():
  
  #Instantiasi queue
  q = queue_Akademik()
  
  while True:
    print("===== Sistem Antrian Akademik =====")
    print("1. Tambah Mahasiswa")
    print("2. Layani Mahasiswa")
    print("3. Lihat Antrian")
    print("4. Keluar")
    
    pilihan = input("Pilih Menu (1-4) : ").strip()
    
    if pilihan == "1" :
      data_nim = input("Masukan Nim : ").strip()
      data_nama = input("Masukan Nama : ").strip()
      
      q.enqueue(data_nim, data_nama)
      print("Mahasiswa Berhasil ditambahkan")
      
    elif pilihan == "2":
      dilayani = q.dequeue()
      print(f"Mahasiswa Dilayani  : {dilayani.nim} - {dilayani.nama}")
    
    elif pilihan == "3":
      q.tampilkan()
      
    elif pilihan == "4":
      print("Program Selesai. Terima Kasih")
      break
    
    else:
      print("Pilihan Tidak Valid. Silahkan coba lagi 1-4")

# Penanda eksekusi file utama
if __name__ == "__main__":
  main()
      
    
  

  
  




