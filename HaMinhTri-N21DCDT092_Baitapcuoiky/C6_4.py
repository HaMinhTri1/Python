
def hop(a, b):
    # Loại bỏ các phần tử trùng nhau trong mảng a và b
    unique_a = a
    unique_b = b
    result = sorted(set(unique_a + unique_b))
    return result
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = hop(a, b)
print(c)  
