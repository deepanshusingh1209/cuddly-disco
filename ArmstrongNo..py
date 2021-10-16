Number1 = int(input("Give the Number "))
for Number in range(Number1, Number1 + 1):
    y = 0
    x = 0
    i = Number
    if (i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9):
        print(Number, "is not a Armstrong no.")
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
        print(Number, "is a Armstrong no.")
    else:
        print(Number, "is not a Armstrong no.")
#'''115132219018763992565095597973971522401 is biggest armstrong number'''
