total= 0
count =0
while(True):
    inp = input('Enter a number:')#Nhap vao 1 so
    if inp == 'done': break#thoat vong lap sau khi nhap done
    value = float(inp) #mac dinh kieu float cho so nhap vao bien inp
    total = total + value #cong value vao total
    count = count +1#bien count tang len 1
    average = total / count#lay bien total chia cho count
print('Average: ',average)