def poT(n):
    if n==0:
        return 1
    else:
        power = poT(n-1)
        return power *2
a=poT(3)
print(a)