def printUPS(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,2):
                print(str(arrayA[i])+","+str(arrayB[j]))
a=[0,1,2,3]
b=[1,2,3,4]
printUPS(a,b)