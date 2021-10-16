from datetime import date
from datetime import time
from datetime import datetime
t1 = datetime.now()
Max_Number = 10*100
y= 0
x = 0
for Number in range (0,Max_Number):
    i = Number
    while i > 0:
                x = x + 1
                i = i // 10
    i = Number
    while i > 0:
                Reminder = i % 10
                y= y + (Reminder ** x)
                i //= 10
    if Number == y:
            print(Number,"is a Armstrong no.")
t2 = datetime.now()
t3 = t2 - t1
print("time taken is "+ str(t3))
#'''115132219018763992565095597973971522401 is biggest armstrong number'''

