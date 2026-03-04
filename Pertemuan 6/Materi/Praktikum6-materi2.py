# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ================================================
# Insertion Sort (Ascending)
# ================================================


def insertion_sort(data):
  
  # Melihat data
  print("Data Awal  : ", data)
  print("="*50)
  
  # Loop mulai dari data ke 2 (Index array ke 1)
  for i in range(1, len(data)):
    
    
    key = data[i] # Simpan nilai yg disisipkan 
    j = i - 1 # Index elemen terakhir di bagian kiri
    
    print("Iterasi ke -", i)
    print("Nilai key =", key)
    print("Bagian Kiri (terurut) :", data[:i])
    print("Bagian Kanan (Belum terurut):", data[i:])
    
    # Geser
    while j >= 0 and data [j] > key:
      data[j+1] = data[j]
      j -= 1  
    # Sisipkan Key ke posisi yang benar
      data[j+1] = key
      
      print("Setelah disisipkan :", data)
      print("="*50)
    return data
       
angka = [7,8,5,2,4,6]
print("Hasil Sorting  :", insertion_sort(angka))