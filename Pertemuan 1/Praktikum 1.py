#============================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#============================================================================

#Contoh 1

with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
  data = file.read()
print(data)

#Contoh 2
#file = open("Data Mahasiswa.txt", "r", encoding = "UTF-8")
#data = file.read()
#print(data)

print("===Hasil Read===")
print("Tipe data :", type(data))
print("Jumlah Karakter :", len(data))
print("Jumlah Baris", data.count("\n")+1)

#Membaca File per Baris
#Latihan Dasar 2A : Membaca seluruh isi file
jumlah_baris = 0
with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
  for baris in file:
    jumlah_baris += 1
    baris = baris.strip()
    print("Baris ke-", jumlah_baris)
    print("Isinya :", baris)
  
with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
  for baris in file:
    baris = baris.strip()
    nim, nama, nilai = baris.split(",")
    print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)

#Latihan Dasar 3A : Membaca file dan menyimpan dalam list

data_list = []
with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
  for baris in file:
    baris = baris.strip()
    nim, nama, nilai = baris.split(",")
    data_list.append([nim, nama, int(nilai)])
  
print("=====Data Mahasiswa Dalam List=====")
print(data_list)
print("=====Jumlah Record Dalam List=====")
print("Jumlah Record", len(data_list))
print("Contoh Record Pertama: ", data_list[0])

#Latihan Dasar 3A : Membaca file dan menyimpan dalam dictionary

data_dict = {}
with open("Data Mahasiswa.txt", "r", encoding = "UTF-8") as file:
  for baris in file:
    baris = baris.strip()
    nim, nama, nilai = baris.split(",")
    data_dict[nim] = {
      "Nama" : nama,
      "Nilai" : nilai
    }
print("=====Data Mahasiswa Dalam Dictrionary=====")
print(data_dict)