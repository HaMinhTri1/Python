def hammu(x,n):
    if n==0:
        return 1
    else:
        x=x * x**(n-1)
        return x
a=hammu(2,8)
print(a)