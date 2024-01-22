import array as arr 
a = arr.array('i', [2, 5, 6, 8]) 
def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i], "," , array[j])

printUnorderedPairs(a)
            