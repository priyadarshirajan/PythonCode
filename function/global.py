def f1():
    global name 
    name = input("Enter your name :")

def f2():
    f1()
    print(name)

f2()