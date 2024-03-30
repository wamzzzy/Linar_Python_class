#Build a software that will tell the user's the maximum amount of loan that they can request based on their monthly salary and if they have an outstanding debt by collecting the user's monthly salary
#And tell the users how much they are to pay back after requesting for a loan(by calculating 20% of their loan and adding it to their loan)
#Users that are not up to 18 will not be eligible for a loan. 
#Users that earn between 10k-below 50k will get 10% of their monthly salary as the maximum amount of loan they can request for
#Users that earn between 50k-below 100k will get 20% of their monthly salary as the maximum amount of loan they can request for
#Users that earn between 100k-below 500k will get 30% of their monthly salary as the maximum amount of loan they can request for
#Users that earn between 500k-below 1m will get 40% of their monthly salary as the maximum amount of loan they can request for
#Users that earn between 1m-below 10m will get 50% of their monthly salary as the maximum amount of loan they can request for
#Users that earn 10m above as their monthly salary will get 50% of 10m as the maximum amount of loan they can request for
#Users that earn less than 10k will not be eligible for loan

print("Hell0!\nWelcome to Loan Approval Software")

name = input("Enter your name: ")
age = int(input("Enter your age (figures only): "))
if age < 18:
    print("Sorry, you are not eligible for a loan")

elif age >= 18:
    salary = int(input("Enter your salary: "))

    #calculating each salary percentage for maximum loan amount
    loan1 = int(salary*(10/100))
    loan2 = int(salary*(20/100))
    loan3 = int(salary*(30/100))
    loan4 = int(salary*(40/100))
    loan5 = int(salary*(50/100))
    loan6 = int(10000000*(50/100))

    loan_debt = input("Do you have an outstanding loan debt? (Yes/No): ")

    #calculating the loan package for user's with outstanding debt
    if loan_debt.upper()=='YES':
        loan_debt_amount = int(input("How much is your debt?(figures only) "))

        #calculating each salary percentage for maximum loan amount for user's with outstanding debt
        loan7 = loan1-loan_debt_amount
        loan8 = loan2-loan_debt_amount
        loan9 = loan3-loan_debt_amount
        loan10 = loan4-loan_debt_amount
        loan11 = loan5-loan_debt_amount
        loan12 = loan6-loan_debt_amount

        if salary<10000:
            print("Sorry, you are not eligible to request for a loan due to your low salary")
        elif salary>=10000 and salary<50000:
            print(f'The maximum loan amount you can request for is {loan7} naira')
            loan_amount1 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount1 and loan_amount1<=loan7:
                interest1 = int((loan_amount1*(20/100))+loan_debt_amount+loan_amount1)
                print(f'Your loan request is approved and You are to pay back {interest1} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=50000 and salary<100000:
            print(f'The maximum loan amount you can request for is {loan8} naira')
            loan_amount2 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount2 and loan_amount2<=loan8:
                interest2 = int((loan_amount2*(20/100))+loan_debt_amount+loan_amount2)
                print(f'Your loan request is approved and You are to pay back {interest2} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=100000 and salary<500000:
            print(f'The maximum loan amount you can request for is {loan9} naira')
            loan_amount3 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount3 and loan_amount3<=loan9:
                interest3 = int((loan_amount3*(20/100))+loan_debt_amount+loan_amount3)
                print(f'Your loan request is approved and You are to pay back {interest3} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=500000 and salary<1000000:
            print(f'The maximum loan amount you can request for is {loan10} naira')
            loan_amount4 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount4 and loan_amount4<=loan10:
                interest4 = int((loan_amount4*(20/100))+loan_debt_amount+loan_amount4)
                print(f'Your loan request is approved and You are to pay back {interest4} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=1000000 and salary<10000000:
            print(f'The maximum loan amount you can request for is {loan11} naira')
            loan_amount5 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount5 and loan_amount5<=loan11:
                interest5 = int((loan_amount5*(20/100))+loan_debt_amount+loan_amount5)
                print(f'Your loan request is approved and You are to pay back {interest5} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=10000000:
            print(f'The maximum loan amount you can request for is {loan12} naira')
            loan_amount6 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount6 and loan_amount6<=loan12:
                interest6 = int((loan_amount6*(20/100))+loan_debt_amount+loan_amount6)
                print(f'Your loan request is approved and You are to pay back {interest6} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        else:
            print('Invalid Salary\nPlease enter correct salary')

    #calculating the loan package for user's without outstanding debt
    elif loan_debt.upper()=='NO':
        if salary<10000:
            print("Sorry, you are not eligible to request for a loan")
        elif salary>=10000 and salary<50000:
            print(f'The maximum loan amount you can request for is {loan1} naira')
            loan_amount7 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount7 and loan_amount7<=loan1:
                interest7 = int((loan_amount7*(20/100))+loan_amount7)
                print(f'Your loan request is approved and You are to pay back {interest7} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=50000 and salary<100000:
            print(f'The maximum loan amount you can request for is {loan2} naira')
            loan_amount8 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount8 and loan_amount8<=loan2:
                interest8 = int((loan_amount8*(20/100))+loan_amount8)
                print(f'Your loan request is approved and You are to pay back {interest8} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=100000 and salary<500000:
            print(f'The maximum loan amount you can request for is {loan3} naira')
            loan_amount9 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount9 and loan_amount9<=loan3:
                interest9 = int((loan_amount9*(20/100))+loan_amount9)
                print(f'Your loan request is approved and You are to pay back {interest9} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=500000 and salary<1000000:
            print(f'The maximum loan amount you can request for is {loan4} naira')
            loan_amount10 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount10 and loan_amount10<=loan4:
                interest10 = int((loan_amount10*(20/100))+loan_amount10)
                print(f'Your loan request is approved and You are to pay back {interest10} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        elif salary>=1000000 and salary<10000000:
            print(f'The maximum loan amount you can request for is {loan5} naira')
            loan_amount11 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount11 and loan_amount11<=loan5:
                interest11 = int((loan_amount11*(20/100))+loan_amount11)
                print(f'Your loan request is approved and You are to pay back {interest11} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")
            
        elif salary>=10000000:
            print(f'The maximum loan amount you can request for is {loan6} naira')
            loan_amount12 = int(input("Enter the loan amount you want to request for(figures only): "))
            if 0<loan_amount12 and loan_amount12<=loan6:
                interest12 = int((loan_amount12*(20/100))+loan_amount12)
                print(f'Your loan request is approved and You are to pay back {interest12} naira')
            else:
                print("You can't request for that amount. Enter eligible amount")

        else:
            print('Invalid Salary\nPlease enter correct salary')

    else:
        print("Please enter correct option")



