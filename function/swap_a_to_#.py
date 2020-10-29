def Swap(char):
    l = []
    for letter in char:
        if letter == "a":
            l.append("#")
        else:
            l.append(letter)
    for i in l:
        print(i,end="")
char = input("Enter any name :")
Swap(char)


