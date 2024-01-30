numsDays = int(input('So ngay tinh nhiet do: '))
t = 0
temp = []
for i in range(numsDays):
    nD = int(input('Nhiet do ngay ' + str(i+1) +' la: '))
    temp.append(nD)
    t += nD
avg = round(t/numsDays,2)
print('Nhiet do trung binh: '+ str(avg))

above = 0
for i in temp:
    if i > avg:
        above +=1

print(str(above)+'ngay tren nhiet do trung binh')