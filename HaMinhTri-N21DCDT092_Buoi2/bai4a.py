def printUP(arrayA,arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i])+","+str(arrayB[j]))
arraya=[1,2,3]
arrayb=[2,3,4]
printUP(arraya,arrayb)