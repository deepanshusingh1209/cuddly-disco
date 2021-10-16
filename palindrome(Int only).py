n=int(input("give a input : "))
a=n
s=0
while (n>0):
    r= n%10
    n = n//10
    s=s*10 + r
print("reverse is" , s)
if(a==s):
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")