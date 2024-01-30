mylist = [1,2,3,4,5,6,7,8,9,10]
target = 55
if target in mylist:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")
def linear_search(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1
print(linear_search(mylist,target))
