n = int(input("How many day's temperature?"))
a=[]
if n <= 0:
    exit()
for i in range(n):
    a.append(int(input("Day %i high temp: " %(i+1))))
avg=sum(a)/len(a)
print("Average: ",avg)
for i in a:
    s=0
    if i > avg:
        s=s+1
        print(s," day(s) is above average")