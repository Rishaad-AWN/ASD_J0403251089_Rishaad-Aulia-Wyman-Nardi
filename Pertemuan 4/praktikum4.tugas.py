# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# Struktur Data: Queue (FIFO) berbasis Linked List
# ==========================================================

# ----------------------------------------------------------
# 1) Definisi Node
#    Menyimpan data pelanggan: nomor antrian, nama, jenis servis
# ----------------------------------------------------------
class Node:
    def __init__(self, no, nama, servis):
        self.no     = no      # nomor antrian pelanggan
        self.nama   = nama    # nama pelanggan
        self.servis = servis  # jenis servis yang diminta
        self.next   = None    # pointer ke node berikutnya

# ----------------------------------------------------------
# 2) Definisi Queue berbasis Linked List
#    front: node paling depan (dilayani lebih dulu)
#    rear : node paling belakang (tempat masuk data baru)
# ----------------------------------------------------------
class QueueBengkel:
    def __init__(self):
        self.front = None  # awalnya queue kosong
        self.rear  = None

    def is_empty(self):
        # Queue kosong jika front = None
        return self.front is None

    def enqueue(self, no, nama, servis):
        # Menambahkan pelanggan baru ke BELAKANG antrian (rear)
        node_baru = Node(no, nama, servis)  # buat node baru

        if self.is_empty():
            # Jika queue kosong, front dan rear sama-sama menunjuk node baru
            self.front = node_baru
            self.rear  = node_baru
            return

        # Jika queue tidak kosong:
        # rear lama menunjuk node baru, lalu rear berpindah ke node baru
        self.rear.next = node_baru
        self.rear      = node_baru
        print("Pelanggan berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # Melayani (mengambil & menghapus) pelanggan dari DEPAN antrian (front)
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan yang bisa dilayani.")
            return

        # Ambil data pelanggan di front
        node_dilayani = self.front

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah geser front menjadi None, queue kosong
        # maka rear juga harus None
        if self.front is None:
            self.rear = None

        print(f"Melayani: No.{node_dilayani.no} | {node_dilayani.nama} | Servis: {node_dilayani.servis}")

    def tampilkan(self):
        # Menampilkan seluruh isi antrian dari front ke rear
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("\nDaftar Antrian Bengkel (Front -> Rear):")
        current = self.front
        no_urut = 1
        # Traversal dari front sampai None
        while current is not None:
            print(f"{no_urut}. No.{current.no} | {current.nama} | Servis: {current.servis}")
            current = current.next
            no_urut += 1

# ----------------------------------------------------------
# 3) Program Utama (Menu Interaktif)
# ----------------------------------------------------------
def main():
    q = QueueBengkel()  # membuat objek antrian bengkel

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no     = input("No Antrian : ")
            nama   = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid")

# ----------------------------------------------------------
# 4) Penanda eksekusi file utama
# ----------------------------------------------------------
if __name__ == "__main__":
    main()
