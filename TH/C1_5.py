def ss(n):
    if n == sum:
        print("perfect")
    elif n > sum:
        print("deficient")
    else:
        print("abudant")
print("Nhap x: ")
x = int(input())
print("Nhap Y: ")
y = int(input())
n = x
for i in range(x,y+1):
    sum = 0
    a = n + i - x
    for e in range(1, a ):
      if (a % e == 0):
        sum += e
    print("so ",a)
    print(sum)
    ss(a)
    
