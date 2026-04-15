data = [80, 90, 10, 30, 204, 50 ,60]

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    middle = len(data) // 2
    left_part = data[:middle]
    right_part = data[middle:]
    
    left = merge_sort(left_part)
    right = merge_sort(right_part)
    return merge(left, right)    

def merge(left, right):
    result = []
    p = q = 0
    
    while p < len(left) and q < len(right):
        if left[p] <= right[q]:
            result.append(left[p])
            p += 1
        else:
            result.append(right[q])
            q += 1

    result.extend(left[p:]) 
    result.extend(right[q:])
    return result
print(merge_sort(data))
    
