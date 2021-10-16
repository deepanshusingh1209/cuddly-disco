from datetime import date
from datetime import time
from datetime import datetime
t1 = datetime.now()
num = int(input("enter a no."))
if (num < 0):
    print("sry")
elif(num == 0):
    print("the factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num+1,):
        factorial = factorial*i
    print("Factorial of ", num, "is", factorial)
t2 = datetime.now()
t3 = t2 - t1
print("time taken is " + str(t3))
