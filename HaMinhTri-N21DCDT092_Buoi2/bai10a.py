def pO2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev=pO2(int(n/2))
        curr=prev *2
        print(curr)
        return curr
print(pO2(16))