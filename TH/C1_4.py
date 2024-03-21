def Pascal(n):
    for i in range(n + 1):
        hs= 1
        for j in range(1, i + 2):
            print(hs, end=" ")
            hs = hs* (i - j + 1) // j
        print()

n = int(input("Nhap so nguyen duong : "))
if n < 0:
    print("n khong phai la so nguyen duong.")
else:
    print("Tam giac pascal bac", n, "la:")
    Pascal(n)