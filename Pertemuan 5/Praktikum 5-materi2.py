#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Materi Rekrusif : Call Stack
# Tracing Bilangan : (Masuk-Keluar)
# Input 3
# Masuk 3-2-1 | 1-2-3
# Keluar
#======================================================

def hitung(n):
  if n == 0:
    print("Selesai")
    return
  
  print("Masuk :", n)
  hitung(n-1) # Recrusive Case
  print("Keluar :", n)

print("===== Program Tracing =====")
hitung(3)




