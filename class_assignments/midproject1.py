#Build a software that will tell the user's the maximum amount of loan that they can request based on their monthly salary by collecting the user's monthly salary
#User's that earn between 10k-below 50k will get 10% of their monthly salary as the maximum amount of loan they can request for
#User's that earn between 50k-below 100k will get 20% of their monthly salary as the maximum amount of loan they can request for
#User's that earn between 100k-below 500k will get 30% of their monthly salary as the maximum amount of loan they can request for
#User's that earn between 500k-below 1m will get 40% of their monthly salary as the maximum amount of loan they can request for
#User's that earn between 1m-below 10m will get 50% of their monthly salary as the maximum amount of loan they can request for
#User's that earn 10m above as their monthly salary will get 50% of 10m as the maximum amount of loan they can request for
#User's that earn less than 10k will not be eligible for loan

print("Hell0!\nWelcome to Loan Approval Software")

name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

#calculating each salary percentage
loan1 = int(salary*(10/100))
loan2 = int(salary*(20/100))
loan3 = int(salary*(30/100))
loan4 = int(salary*(40/100))
loan5 = int(salary*(50/100))
loan6 = int(10000000*(50/100))

#printing the result for each conditions
if salary<10000:
    print("Sorry, you are not eligible to request for a loan")
elif salary>=10000 and salary<50000:
    print(f'The maximum amount you can request for is {loan1} naira')
elif salary>=50000 and salary<100000:
    print(f'The maximum amount you can request for is {loan2} naira')
elif salary>=100000 and salary<500000:
    print(f'The maximum amount you can request for is {loan3} naira')
elif salary>=500000 and salary<1000000:
    print(f'The maximum amount you can request for is {loan4} naira')
elif salary>=1000000 and salary<10000000:
    print(f'The maximum amount you can request for is {loan5} naira')
elif salary>=10000000:
    print(f'The maximum amount you can request for is {loan6} naira')
else:
    print('Invalid Salary\nPlease enter correct salary')