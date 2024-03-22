#Build a function that will grade waec and neco score by taking the user's name, school, year of exam, exam name, score and will tell them when to get their result for each exam.


def welcome(name = input('Enter your name: '),school = input('Enter your school: '),year_of_exam = int(input('Enter year of exam: ')),exam = input('Enter exam name (in capital letters): ')):
    """This function helps to grade user's waec and neco score and tell the user when to get their result by taking the user's name, school, year of exam, name of exam and score."""
    print(f'Welcome {name}, you attended {school}. You took {exam} in {year_of_exam}. This software will help you grade your scores.')
    if exam.upper() == 'WAEC':
        waec_grade(score = int(input("Enter your WAEC score: ")))
        waec_result_year(year_of_exam)
    elif exam.upper() == 'NECO':
        neco_grade(score = int(input("Enter your NECO score: ")))
        neco_result_year(year_of_exam)
    else:
        print('Invalid exam name; enter correct exam name')


def waec_grade(score):
    """This function helps to grade the user's waec score."""
    if score>=0 and score<=39:
        print("Your grade is Fail")
    elif score>=40 and score<=44:
        print("Your grade is Poor")
    elif score>=45 and score<=49:
        print("Your grade is Pass")
    elif score>=50 and score<=59:
        print("Your grade is Good")
    elif score>=60 and score<=69:
        print("Your grade is Very Good")
    elif score>=70 and score<=100:
        print("Well done! Your grade is Excellent")
    else:
        print("Invalid score for WAEC")

def waec_result_year(year_of_exam):
    """This function tells the user's when to get their waec result"""
    result_year = year_of_exam + 4
    print(f'You will get your result in {result_year}')

def neco_grade(score):
    """This function helps to grade the user's neco score"""
    if score>=0 and score<=10:
        print("Your grade is Fail")
    elif score>=11 and score<=29:
        print("Your grade is Poor")
    elif score>=30 and score<=39:
        print("Your grade is Pass")
    elif score>=40 and score<=59:
        print("Your grade is Good")
    elif score>=60 and score<=79:
        print("Your grade is Very Good")
    elif score>=80 and score<=100:
        print("Well done! Your grade is Excellent")
    else:
        print("Invalid score for NECO")

def neco_result_year(year_of_exam):
    """This function tells the user's when to get their waec result"""
    result_year = year_of_exam + 5
    print(f'You will get your result in {result_year}')
    
    


welcome()