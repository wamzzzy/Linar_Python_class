def agefunction(name= input('Enter your name: '),YOB= input('Enter your year of birth: '),present_year = input('Enter present year: ')):
    """This function helps to calculate the user's age"""
    age = int(present_year) - int(YOB)
    print(f'You are {age} year old')

agefunction()