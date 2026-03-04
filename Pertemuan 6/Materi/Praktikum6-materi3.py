# ================================================
# NAMA : Rishaad Aulia Wyman Nardi
# NIM  : J0403251089
# Kelas: B2
# ================================================

# ================================================
# Merge Sort (Ascending)
# ================================================


def merge_sort(data):
  
  if len(data) <= 1:
    return data
  
  # Divide : Membagi data menjadi 2 bagian
  mid = len(data)//2
  left = data[:mid] # Slicing Bagian Kiri
  right = data[mid:] # Slicing Bagian Kanan
  
  # 8 ==> left 4  right 4
  # left 4 ==> mergesort ==>
  #   left 2 ==> mergesort  
  
  # Recrusive call
  
  left_sorted = merge_sort(left)
  right_sorted = merge_sort(right)
  
  return merge(left_sorted, right_sorted)
  
def merge(left, right):
  
  result = []
  i = 0 
  j = 0
  
  # Membandingkan elemen kiri dan kanan
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
      
  # Menambahkan sisa elemen jika
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result
  
angka = [13,7,28,5,19,36,4]

print("Hasil Sorting  :", merge_sort(angka))



