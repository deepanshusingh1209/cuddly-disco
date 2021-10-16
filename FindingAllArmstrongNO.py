# from datetime import datetime
# t1 = datetime.now()
Min_Number = int(input("GIVE No.1 :-- "))
Max_Number = int(input("Give No.2 :-- "))
n = 1
for Number in range(Min_Number, Max_Number):
    y = 0
    x = 0
    i = Number
    if (i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
        continue
    while i > 0:
        x = x + 1
        i = i // 10
    i = Number
    while i > 0:
        Reminder = i % 10
        y = y + (Reminder ** x)
        i //= 10
    if Number == y:
        print("ARMSTRONG NUMBER ", n, ":-- ", Number, sep="")
        n += 1
    # t2 = datetime.now()
    # t3 = (t2 - t1)
    # print(t3)
    # print("there are " + str(no) + " Armstrong numbers between " +
    #       " 0 " + " and " + str(Max_Number))
    #'''115132219018763992565095597973971522401 is biggest armstrong number'''
