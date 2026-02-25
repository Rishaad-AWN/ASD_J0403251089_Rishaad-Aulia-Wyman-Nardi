#======================================================
# Nama  : Rishaad Aulia Wyman Nardi
# NIM   : J0403251089
# Kelas : B2
#======================================================

# Materi Rekrusif : Faktorial
# Recrusive Case => 3! = 3 x 2 x 1
# Base Case => 0 Berhenti
#======================================================

def faktorial(n):
  # Base Case
  if n == 0:
    return 1
  else:
    return n*faktorial(n-1) # n-1*n-2*n-3 ...........

print("===== Program Faktorial =====")
print("Hasil Faktorial :", faktorial(5))