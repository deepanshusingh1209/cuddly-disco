a=1
i=1
while a<=7:
    while i<=a:
        print(i,end="")
        i+=1
    else:
        print("*"*(7-a))
        a+=1
        i=1