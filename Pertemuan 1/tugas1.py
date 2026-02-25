# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
        - stok_dict (dictionary)
          key = kode_barang
          value = {"nama": nama_barang, "stok": stok_int}
    """
    stok_dict = {}
    
    # Buka file dan baca seluruh baris
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                # Gunakan strip() untuk hilangkan \n
                baris = baris.strip()
                
                # Lewati baris kosong
                if baris == "":
                    continue
                
                # Split(",") untuk pisah kolom
                parts = baris.split(",")
                
                # Pastikan format benar (3 kolom)
                if len(parts) != 3:
                    continue
                
                kode, nama, stok_str = parts
                
                # Konversi stok ke integer
                try:
                    stok_int = int(stok_str)
                except ValueError:
                    continue
                
                # Simpan ke dictionary
                stok_dict[kode] = {"nama": nama, "stok": stok_int}
    
    except FileNotFoundError:
        # Jika file tidak ada, kembalikan dictionary kosong
        pass
    
    return stok_dict

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # Tulis ulang seluruh isi file berdasarkan stok_dict
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            f.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    # Jika kosong, tampilkan pesan stok kosong
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return
    
    # Tampilkan dengan format rapi: kode | nama | stok
    print("\n=========== DAFTAR SEMUA BARANG ===========")
    print(f"{'Kode':<12} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 43)
    
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<12} | {nama:<20} | {stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()
    
    # Cek apakah kode ada di dictionary
    if kode in stok_dict:
        # Jika ada: tampilkan detail barang
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode       : {kode}")
        print(f"Nama Barang: {nama}")
        print(f"Stok       : {stok}")
    else:
        # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
        print("Barang tidak ditemukan")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang: ").strip()
    
    # Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
        print("Kode sudah digunakan")
        return
    
    # Input stok awal (integer)
    try:
        stok_awal = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return
    
    # Validasi stok tidak boleh negatif
    if stok_awal < 0:
        print("Stok tidak boleh negatif.")
        return
    
    # Simpan ke dictionary
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print(f"Barang '{nama}' berhasil ditambahkan.")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    # Cek apakah kode ada di dictionary
    if kode not in stok_dict:
        # Jika tidak ada: tampilkan pesan dan return
        print("Kode barang tidak ditemukan.")
        return
    
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    # Input jumlah perubahan stok
    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    
    # Validasi jumlah tidak boleh negatif
    if jumlah < 0:
        print("Jumlah tidak boleh negatif.")
        return
    
    # Proses update berdasarkan pilihan
    if pilihan == "1":
        # Jika pilihan 1: stok = stok + jumlah
        stok_dict[kode]["stok"] += jumlah
        print(f"Stok berhasil ditambah. Stok sekarang: {stok_dict[kode]['stok']}")
    
    elif pilihan == "2":
        # Jika pilihan 2: stok = stok - jumlah
        stok_baru = stok_dict[kode]["stok"] - jumlah
        
        # Jika hasil < 0: batalkan dan tampilkan error
        if stok_baru < 0:
            print("Stok tidak mencukupi. Update dibatalkan.")
            return
        
        stok_dict[kode]["stok"] = stok_baru
        print(f"Stok berhasil dikurangi. Stok sekarang: {stok_dict[kode]['stok']}")
    
    else:
        print("Pilihan tidak valid.")

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)
    
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        
        elif pilihan == "2":
            cari_barang(stok_barang)
        
        elif pilihan == "3":
            tambah_barang(stok_barang)
        
        elif pilihan == "4":
            update_stok(stok_barang)
        
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        
        elif pilihan == "0":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()