def Duynhat(a):
    unique_elements = list(set(a))
    b = sorted(unique_elements) 
    return b
a = [1, 5, 3, 7, 5, 9, 7]
result = Duynhat(a)
print("Mảng b sau sắp xếp:", result)
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
def sapxep(a):
    b = []
    for i in arr:
          if i not in b:
            b.append(i)
    return b
# Example usage
arr = [12, 11, 13, 5, 6, 7,11]
print("Given array:", arr)
mergeSort(arr)
b = sapxep(arr)
print("Sorted array:", b)
