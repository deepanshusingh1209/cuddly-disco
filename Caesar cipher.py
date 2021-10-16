a=str(input("Tell the Word u wants to encrypt :--"))
b=int(input("(-ve) integers will indicate left shift\n                   &\n(+ve) inetegrs will indicate right shift \nNow, Tell how much character shift u want :-- "))
a1=list(a)
a2=[]
i=0
lenght_of_a1 = len(a1)
while i<lenght_of_a1 :
    n=a1[i]
    c=(ord(n)+(b))
    d=chr(c)
    a2.append(d)
    i+=1
else:
    a3=' '.join(a2)
    a3 = a3.replace(" ","")
    print("After encrypting",a,"we will get",a3)