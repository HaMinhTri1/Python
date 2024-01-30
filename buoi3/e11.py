prev_list = [-1,10,-20,2,-30,77,56,32,-8,0]
new_list = [number if number > 0 else 0 for number in prev_list]
print(new_list)
