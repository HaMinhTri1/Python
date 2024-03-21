def fibonacci(n):
    assert n >= 0 and int(n) == n
    if n in [0,1]:
        return n
    else:
        return fibonacci (n-1) + fibonacci(n-2)

s = fibonacci(5)
print(s) 

#C
def fibonacci1(n):
    assert n >= 0 and int(n) == n
    if n in [0,1]:
        return n
    else:
        a = 0
        b = 1 
        c = 1 
        for i in range(2,n):
            a = b
            b = c
            c = a + b
        return c
print(fibonacci1(6))        

            