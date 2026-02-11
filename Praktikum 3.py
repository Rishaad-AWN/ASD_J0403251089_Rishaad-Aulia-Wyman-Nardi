class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        if not self.head:
            print("\nList kosong!")
            return
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def display_backward(self):
        if not self.tail:
            print("\nList kosong!")
            return
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

    def delete_node(self, key):
        temp = self.head
        
        # Jika list kosong
        if not temp:
            print("List kosong! Tidak ada yang bisa dihapus.")
            return
        
        # Jika node pertama yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            print(f"Data {key} berhasil dihapus!")
            return
        
        # Cari node yang akan dihapus
        while temp and temp.data != key:
            temp = temp.next
        
        # Jika tidak ditemukan
        if temp is None:
            print(f"Data {key} tidak ditemukan!")
            return
        
        # Update pointer
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        else:
            self.tail = temp.prev
        
        print(f"Data {key} berhasil dihapus!")

    def search_node(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                return f"Data {key} ditemukan di posisi ke-{position}!"
            temp = temp.next
            position += 1
        return f"Data {key} tidak ditemukan!"
      
    def reverse_node(self):
        if not self.head:
            print("List kosong!")
            return
        
        temp = None
        current = self.head
        self.tail = self.head
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev
        
        print("List berhasil dibalik!")

def main():
    ll = DoublyLinkedList()
    
    while True:
        print("\n" + "="*50)
        print("       PROGRAM DOUBLY LINKED LIST")
        print("="*50)
        print("1. Masukkan Data")
        print("2. Hapus Data")
        print("3. Cari Data")
        print("4. Tampilkan Data (Forward)")
        print("5. Tampilkan Data (Backward)")
        print("6. Balik Urutan Data")
        print("7. Keluar")
        print("="*50)

        try:
            pilihan = int(input("Pilih menu (1-7): "))
            
            if pilihan == 1:
                masuk = int(input("Masukkan angka: "))
                ll.insert_at_end(masuk)
                print(f"Data {masuk} berhasil ditambahkan!")
                
            elif pilihan == 2:
                hapus = int(input("Masukkan angka yang akan dihapus: "))
                ll.delete_node(hapus)
                
            elif pilihan == 3:
                cari = int(input("Masukkan angka yang dicari: "))
                result = ll.search_node(cari)
                print(result)
                
            elif pilihan == 4:
                ll.display_forward()
                
            elif pilihan == 5:
                ll.display_backward()
                
            elif pilihan == 6:
                ll.reverse_node()
                
            elif pilihan == 7:
                print("\n" + "="*50)
                print("                     KELUAR           ")
                print("="*50)
                break
                
            else:
                print("Pilihan tidak valid! Silakan pilih 1-7.")
                
        except ValueError:
            print("Input tidak valid! Masukkan angka saja.")

main()