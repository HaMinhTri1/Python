import array as arr
def hieu(a, b):
    # Loại bỏ các phần tử trùng nhau trong mảng a và b
    unique_a = set(a)
    unique_b = set(b)
    result = sorted(unique_a - unique_b)
    return result
a = arr.array('i',[1, 5, 3, 7, 9, 4, 2])
b = arr.array('i',[9, 6, 2, 3, 8])
c = hieu(a, b)
print(c)  
