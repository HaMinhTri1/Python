def gcd(m,n):
    if n !=0:
        return gcd(n, m % n)
    else:
        return m
m=int(input("Nhập m = "))
n=int(input("Nhập n = "))
print("GCD cua 2 so m,n la: ",gcd(m,n))
def fibonacci_ko_de_quy(n):
    assert n >= 0 and int(n) == n
    if n in [0, 1]:
        return n

    a, b, c = 0, 1, 0
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c
e = fibonacci_ko_de_quy(m,n)
print(e)