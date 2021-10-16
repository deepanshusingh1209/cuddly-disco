num=int(input("enter a no."))
if(num>1):
    for i in range (2,num):
        if(num%i==0):
            print(num,"is not a prime no.")
            print(num,"is",num//i,"times of",i)
            break
    else:
        print(num,"is a prime no.")
