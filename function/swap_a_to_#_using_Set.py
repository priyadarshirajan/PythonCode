conv = (("a","#"), ("b", "*"))
def Swap(character):
    for a,b in conv:
        character = character.replace(a,b)
    return character


char = input("Enter any name :")
res = Swap(char)
print(res)