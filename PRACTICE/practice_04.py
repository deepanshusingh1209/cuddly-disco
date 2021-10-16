T=int(input(""))
i=0
list1=[]
while i<T :
    a=int(input(""))
    list1.append(a)
    i+=1
else:
    i=0
    while i<len(list1):
        b=list1[i]
        b=str(b)
        b=(b[::-1])
        b=int(b)
        print(b)
        i+=1