def Ascii(char):
    ascii_value = []
    for lett in char:
        ascii_value.append(ord(lett))
    return ascii_value

char = input("Enter any charater :")
res = Ascii(char)
print(res)