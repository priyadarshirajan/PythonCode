def Fibo(f=0,s=1):
    for num in range(8):
        print(f ,end=",")
        temp = f + s 
        f = s
        s = temp
Fibo()
