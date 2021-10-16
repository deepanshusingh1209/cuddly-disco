a=str(input("Give input that you wanna check it whether it is poallindromne or not :"))
b=(a[::-1])
if a==b:
    print(a,"is palindrome \nit's palindrome is", b)
else:
    print(a,"is not a palindrome")