# Latihan	1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu. 

class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = NodeSingle(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Data {data} berhasil ditambahkan!")
    
    def display(self):
        if not self.head:
            print("\nList kosong!")
            return
        print("\nIsi Single linked list:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def delete_node(self, key):
        temp = self.head
        
        if not temp:
            print("List kosong! Tidak ada yang bisa dihapus.")
            return
        
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Data {key} berhasil dihapus!")
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print(f"Data {key} tidak ditemukan!")
            return
        
        prev.next = temp.next
        temp = None
        print(f"Data {key} berhasil dihapus!")

ll = SingleLinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_at_end(10)
ll.display()

# Menghapus node dengan nilai tertentu.
ll.delete_node(10)
ll.display()



#  Latihan	3:  Implementasikan Pencarian pada node tertentu Double Linked List.
class NodeDouble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = NodeDouble(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"Data {data} berhasil ditambahkan!")
    
    def display(self):
        if not self.head:
            print("\nList kosong!")
            return
        print("\nIsi Double Linked List:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Fungsi Cari Node Tertentu
    def search_node(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                return f"Data {key} ditemukan di posisi ke-{position}!"
            temp = temp.next
            position += 1
        return f"Data {key} tidak ditemukan!"
    
ll = DoubleLinkedList()
ll.insert_at_end(6)
ll.insert_at_end(3)
ll.insert_at_end(8)
ll.insert_at_end(18)
ll.insert_at_end(20)
ll.display()
# Pencarian node tertentu pada Double Linked List.
print(ll.search_node(8))
print(ll.search_node(17))


# Latihan	5:  Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked baru.

class NodeSingle:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = NodeSingle(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Data {data} berhasil ditambahkan!")
    
    def display(self):
        if not self.head:
            print("\nList kosong!")
            return
        print("\nIsi Single linked list:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
        
    # Fungsi reverse single linked list
    def reverse_list(self):
        if not self.head:
            print("List kosong!")
            return
        
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        
        self.head = prev
        print("List berhasil dibalik!")

ll = SingleLinkedList()
ll.insert_at_end(7)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(9)
ll.insert_at_end(67)
ll.display()
ll.reverse_list()
ll.display()