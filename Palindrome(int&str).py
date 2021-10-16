def ispalindrome(s):
	return s == s[::-1]
s = input("give something ")
ans = ispalindrome(s)
if ans:
	print("Yes")
else:
	print("No")
