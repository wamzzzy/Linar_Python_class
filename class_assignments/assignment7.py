#Build a tax calculator that will calculate 35% of leftover(salary - expenses) of the user.
#By taking the user's name, age, place of work, level, LGA, number of family members, salary, expenses.

print("Hello! Welcome To Tax Calculator")
Name = input("Enter your name: ")
Age = input("Enter your age: ")
Place_of_work = input("Enter your place of work: ")
Level = input("Enter your level: ")
LGA = input("Enter your L.G.A: ")
no_of_family_members = input("Enter the number of your family members: ")
Salary = int(input("Enter your monthly salary (figures only): "))
Expenses = int(input("Enter your monthly expenses (figures only): "))
Leftover = Salary-Expenses
Tax_value = Leftover*(35/100)
print("The tax value of "+str(Name)+" is "+str(float(Tax_value)))