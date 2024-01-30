sentence = 'My name is Elshad'
def is_consonant(letter):
    vowels = 'aoeui'
    return letter.isalpha() and letter.lower() not in vowels
#tra ve ky trong bang chu cai Alphabet ma khong thuoc vowels va viet thuong cac ky tu hoa

consonant = [i for i in sentence if is_consonant(i)]#xet tung ky tu trong sentence theo is_consonant
print(consonant)
