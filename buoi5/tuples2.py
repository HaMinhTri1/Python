newTuples = ('a','b','c','d','e')
for i in range(len(newTuples)):
    print(newTuples[i]) #in tung gia tri tu vong lap for
print('a' in newTuples)# kiem tra phan tu trong tuple
print(newTuples.index('c'))#tra ve vij tri cua phan tu
def searchTuple(p_tuple,element):#tim ky tu va tra ve vi tri cua ky tu trong tuple
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} is found at {i} index"
    return 'The element is not found'

print(searchTuple(newTuples,'a'))
