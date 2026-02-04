#============================================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membuat fungsi load data
#============================================================================

nama_file = "Data Mahasiswa.txt"

#Membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
  data_dict = {} #inisialisasi data dictionary
  with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
    for baris in file:
      baris = baris.strip()
      nim, nama, nilai = baris.split(",")
      data_dict[nim] = {
        "Nama" : nama,
        "Nilai" : nilai
      }
  print("=====Data Mahasiswa Dalam Dictrionary=====")
  return data_dict
buka_data = baca_data_mahasiswa(nama_file)
#print("Jumlah Baris :", len(buka_data))

#============================================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 2A : Fungsi Menampilkan Data
#============================================================================

def tampilkan_data(data_dict):
  print("======== Daftar Mahasiswa ========")
  print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
  print("-" * 32)
  
  '''
  Untuk tampilan yang rapi, atur f-string formating
    {'NIM' : <10} artinya : 
    tampilkan nim <= rata kiri dengan lebar 10 karakter
    {'Nama' : <12} artinya 
    tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    {'Nilai' : >5} artinya :
    tampilkan nilai rata kiri, dengan lebar kolom 5 karakter
  '''  
  
  for nim in sorted(data_dict.keys()):
    nama = data_dict[nim]["Nama"]
    nilai = data_dict[nim]["Nilai"]
    print(f"{nim : <10} | {nama : <12} | {nilai : >5}")
#Memanggil Fungsi Menampilkan Data
#tampilkan_data(buka_data)


#============================================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 3A : Membuat Fungsi Mencari Data
#============================================================================

def cari_data(data_dict):
  #Mencari data mahasiswa berdasarkan NIM
  nim_cari = input("Masukan NIM yang ingin dicari : ").strip()

  if nim_cari in data_dict:
    nama = data_dict[nim_cari]["Nama"]
    nilai = data_dict[nim_cari]["Nilai"]
    
    print("======== DATA MAHASISWA DITEMUKAN ========")
    print(f"NIM     : {nim_cari}")
    print(f"NAMA    : {nama}")
    print(f"NILAI   : {nilai}")
  else:
    print("Data Tidak Ditemukan")
    
#cari_data(buka_data)

#============================================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 4A : Membuat Fungsi Update Nilai
#============================================================================

def update_nilai(data_mahasiswa_dict):
    #mengupdate nilai mahasiswa berdasarkan NIM
    nim= input("Masukkan NIM yang ingin diupdate nilainya: ").strip()

    if nim not in data_mahasiswa_dict:
        print("Data NIM tidak ditemukan")
        return
    try:
        nilai_baru= int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Input nilai tidak valid, harus berupa angka")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100")
       
    nilai_lama= data_mahasiswa_dict[nim]['Nilai']
    data_mahasiswa_dict[nim]['Nilai'] = nilai_baru
    print(f"\n=======Update Berhasil: Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}===========")

#memanggil fungsi update_nilai_mahasiswa
#update_nilai(buka_data)

#Cara lain update
'''
def update_nilai(data_dict):
  nim = input("Masukan NIM yang ingin dicari untuk ganti nilainya : ").strip()
  
  if nim in data_dict:
    nama = data_dict[nim]["Nama"]
    nilai = data_dict[nim]["Nilai"]
    nilai = int(input("Masukan Nilai Baru (0-100): "))
    data_dict[nim]["Nilai"] = nilai
    if nilai == ValueError:
      print("Masukan Nilai INT")
    elif nilai < 0 or nilai > 100:
      print("Masukan di antara 0-100")
    else : 
      print("======== DATA MAHASISWA DIUBAH ========")
      print(f"NIM     : {nim}")
      print(f"NAMA    : {nama}")
      print(f"NILAI   : {nilai}")
  else:
    print("Data Tidak Ditemukan")
#update_nilai(buka_data)
'''

#============================================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latihan Dasar 5A : Fungsi Menyimpan
#============================================================================

def simpan_data_mahasiswa(nama_file, data_mahasiswa_dict):
    with open(nama_file, 'w', encoding='utf-8') as file:
        for nim in sorted(data_mahasiswa_dict.keys()):
            nama= data_mahasiswa_dict[nim]['Nama']
            nilai= data_mahasiswa_dict[nim]['Nilai']
            file.write(f"{nim},{nama},{nilai}\n")

def main():
  buka_data = baca_data_mahasiswa(nama_file)
  while True:
    print("\n=== MENU DATA MAHASISAW ===")
    print("1. Tampilkan Semua")
    print("2. Cari Data Berdasarkan NIM")
    print("3. Update Niali Mahasiswa")
    print("4. Simpan Data Ke File")
    print("5. Keluar")
    
    pilihan = input("Pilihan Menu : ").strip()
    
    if pilihan == "1":
      tampilkan_data(buka_data)
    elif pilihan == "2":
      cari_data(buka_data)
    elif pilihan == "3":
      update_nilai(buka_data)
    elif pilihan == "4":
      simpan_data_mahasiswa(nama_file, buka_data)
    elif pilihan == "5":
      print('Selesai')
      break
    else :
      print("Pilihan Tidak Valid")
  
if __name__ == "__main__":
  main()