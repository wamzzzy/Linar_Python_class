#Build a function that will greet the user and calculate the tax value by calculating 35% user's leftover(monthly salary - monthly expenses).
#By taking the user's name, monthly salary and monthly expenses.  

def welcome_function():
    """This function welcomes the user"""
    print('Hello! Welcome to Tax calculator')
    print(f'January is {taxfunction(input('Enter your name: '),int(input('Enter your monthly salary (Figures only): ')),int(input('Enter your monthly expenses (Figures only): ')))}')
    print(f'February is {taxfunction(input('Enter your name: '),int(input('Enter your monthly salary (Figures only): ')),int(input('Enter your monthly expenses (Figures only): ')))}')

def taxfunction(name,salary,expenses):
    """This function calculate tax for every user 
    by calculating 35% of user's leftover"""
    leftover= salary - expenses
    taxvalue = leftover *(35/100)
    int_taxvalue = int(taxvalue)
    return f'Your tax value is {int_taxvalue}'


welcome_function()