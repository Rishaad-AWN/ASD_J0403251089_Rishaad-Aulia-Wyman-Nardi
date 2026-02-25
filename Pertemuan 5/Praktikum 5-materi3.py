#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Materi Rekrusif : Menjumlahkan Elemen List
#======================================================

def jumalh_list(data, index=0):
  if index == len(data):
    return 0
  
  return data[index] + jumalh_list(data, index+1)
print("===== Program Jumlah List =====")
print(jumalh_list([2,4,5,6,8]))