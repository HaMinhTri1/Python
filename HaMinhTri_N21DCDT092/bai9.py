def gcd(a,b):
    if b !=0:
        return gcd(b, a % b)
    else:
        return a
c=gcd(48,18)
print(c)