def s7(n):
    if n < 10:
        return n
    else:
        n =n//10+ n%10
        return n
a = s7(112)
print(a)