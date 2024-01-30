def get_number(number):
    if number > 0:
        return number
    else:
        return 'negative number'

prev_list = [-1,2,6,7,-5,-66,12]
new_list = [get_number(number) for number in prev_list]#su dung de qui va vong lap tim so duong
print(new_list)