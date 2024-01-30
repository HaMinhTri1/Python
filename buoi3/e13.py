numsDays = int(input('So ngay tinh nhiet do: '))
t = 0
for i in range(1,numsDays+1):
    nD = int(input('Nhiet do ngay ' + str(i) +' la: '))
    t += nD
avg = round(t/nD,2)
print("Nhiet do trung binh = "+ str(avg))