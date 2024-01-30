def isPalindrome(s):
    return s == s[::-1]
s =input('Nhap vao 1 chuoi: ')
ans = isPalindrome(s)
if ans:
    print("La chuoi Palindrome")
else:
    print("khong phai la chuoi Palindrome")