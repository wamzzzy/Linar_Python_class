D_O_B = int(input("DOB: "))
age = 2024-D_O_B
if age>=18:
    print("You are qualified for python class")
else:
    print("You are best qualified for ICT fundamentals")


Salary = int(input("Salary: "))
Big = Salary*(20/100)
Small = Salary*(12/100)
if Salary>=500000:
    print("Save "+str(int(Big)))
else:
    print("Save "+str(int(Small)))