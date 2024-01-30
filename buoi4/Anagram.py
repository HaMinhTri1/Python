s1 = input("Nhap chuoi 1: ")
s2 = input('Nhap chuoi 2: ')
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("2 chuoi la anagrams.") 
    else:
        print("2 chuoi khong phai la anagrams.")
check(s1,s2)