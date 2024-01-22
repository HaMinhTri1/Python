
n = int(input("matrix n: "))
a=[]
for i in range(n):
    for j in range(n):
        a.append([])
        x = float(input("Nhap phan tu thu a[%2d][%2d]: " % (i, j)))
        a[i].append(x)
print("Day so vua nhap la: ")
for i in range(0, n):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
    print()
print("Day so dao la: ")
for i  in range(n):
    for j in range(n):
     temp = a[i][j]
     a[i][j]= a[j][n-i-1]
     a[j][n-i-1] = temp
for i in range(0, n):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
    print()