def Calc():
    res = 0
    while True:
        price = (input("Enter your price :"))

        if (price) == "q":
            print(f"Your total price is {res} thanks for using \n")
            break

        res = int(price) + res
        print(f"Your total price is {res} thanks for using \n")

Calc() 