import array as arr 
a = arr.array('i', [2, 5, 6, 8]) 
def foo(array):
    sum=0
    product=1
    for i in array:
        sum += i
    for i in array:
        product *=i
    print("Sum= "+str(sum)+",Product="+str(product))
foo(a)