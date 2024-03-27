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
c = 0
def doixung(a):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i][j] != a[j][i]:
                print("Ma tran khong doi xung")
            else:
                c = 0           
doixung(a)
print(c)
if c == 0:
    print("Ma tran doi xung")
else:
    print("Ma tran khong doi xung")