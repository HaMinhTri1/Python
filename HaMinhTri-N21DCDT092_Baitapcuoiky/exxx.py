def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j] # copy jth element of S2 as next item of S
            j += 1
def merge_sort(S):
    n = len(S)
    if n < 2:
        return # list is already sorted

    mid = n // 2
    S1 = S[0:mid] # copy of first half
    S2 = S[mid:n] # copy of second half
 # conquer (with recursion)
    merge_sort(S1) # sort copy of first half
    merge_sort(S2) # sort copy of second half
 # merge results
    merge(S1, S2, S)    
a = [1, 5, 3, 7, 5, 9, 7]
b = [1,3,5,7,8]
c = []
result = merge(a,b,c)
print(c)