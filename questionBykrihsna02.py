your_salary=int(input("enter your salary (in rupees) :--"))
years_of_service=int(input("enter your years of service (in years) :--"))
if years_of_service>5:
    new_salary= your_salary + your_salary*5/100
    your_bonus=your_salary*5/100
    print("your net bonus amount is", your_bonus)
    print("Your Salary including bonus is", new_salary)
else :
    print("You are not eligible for the Bonus \nSo, Your Salary without bonus is", your_salary)