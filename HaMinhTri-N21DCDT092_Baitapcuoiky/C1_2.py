def Neper(n):
    assert n >= 0 and int(n) == n
    s = 0
    f = 1
    for k in range(n + 1):
        s += 1 / f
        f = f *(k + 1)  
    return s

n = int(input("Nhập n>=0: "))
print("Tổng Neper là:", Neper(n))