
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
    q = 0
for i in range(n):
    for k in range(i+1,n):
      j = 0
      for j in range(n):
         if a[i][j] == a[k][j]:
            q = q +1
         else:
            q = q * 0
if q == n:
      print("True")
else:
      print("False") 
