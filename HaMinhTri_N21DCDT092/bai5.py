def giaiThua(n):
    assert n>=0 and int(n)==n
    if n in [0,1]:
        return 1
    else:
         return n* giaiThua(n-1)
a = (giaiThua(5))
print(a)