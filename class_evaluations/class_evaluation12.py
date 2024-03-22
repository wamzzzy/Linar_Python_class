#Build a function that will tell the user if they are eligible to vote or not, by taking the user's name and year of birth.
#If the user is not eligible yet, the function will also tell them when the user will be eligible to vote and what year to come back to vote. 

def agefunction(name= input('Enter your name: '),YOB= input('Enter your year of birth: '),present_year = 2024):
    """This function helps the user to know if they are eligible to vote or not by collecting the user's name, year of birth 
    and tells the user when they will be eligible to vote if they are not eligible yet and when to come back to vote."""
    age = int(present_year) - int(YOB)
    if age >= 18:
        print('You are eligible to vote')
    elif age > 0 and age < 18:
        print('You are not eligible to vote')
        eligible_year(age)
        voting_year(age)
    else:
        print('Invalid year. Please enter correct year')

def eligible_year(age):
    """This function helps to know the year the user will be eligible to vote if the user is not eligible yet."""
    if age == 17:
        print(f'You will be eligible to vote in 2025')
    elif age == 16:
        print(f'You will be eligible to vote in 2026')
    elif age == 15:
        print(f'You will be eligible to vote in 2027')
    elif age == 14:
        print(f'You will be eligible to vote in 2028')
    elif age == 13:
        print(f'You will be eligible to vote in 2029')
    elif age == 12:
        print(f'You will be eligible to vote in 2030')
    elif age == 11:
        print(f'You will be eligible to vote in 2031')
    elif age == 10:
        print(f'You will be eligible to vote in 2032')
    elif age == 9:
        print(f'You will be eligible to vote in 2033')
    elif age == 8:
        print(f'You will be eligible to vote in 2034')
    elif age == 7:
        print(f'You will be eligible to vote in 2035')
    elif age == 6:
        print(f'You will be eligible to vote in 2036')
    elif age == 5:
        print(f'You will be eligible to vote in 2037')
    elif age == 4:
        print(f'You will be eligible to vote in 2038')
    elif age == 3:
        print(f'You will be eligible to vote in 2039')
    elif age == 2:
        print(f'You will be eligible to vote in 2040')
    elif age == 1:
        print(f'You will be eligible to vote in 2041')
    else:
        print('')

def voting_year(age):
    """This function helps the user to know the year when to come back to vote if the user is not eligible yet."""
    if age >= 15 and age <= 17:
        print('Come back to vote in 2027')
    elif age >= 11 and age <= 14:
        print('Come back to vote in 2031')
    elif age >= 7 and age <= 10:
        print('Come back to vote in 2034')
    elif age >= 3 and age <= 6:
        print('Come back to vote in 2038')
    elif age >=1 and age <= 2:
        print('Come back to vote in 2042')
    else:
        print('')


    

agefunction()