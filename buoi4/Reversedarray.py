n = int(input("Nhập số phần tử của list : "))
my_list = []
for i in range(n):
   val = input('Nhập giá trị: ')
   my_list.append(val)
print(my_list)
my_list.reverse()
print(my_list)
