#Four examples where you can use while loop

#1
x = 0
while x<5:
    print(x)
    x+=1

#2
first_voting_year = 1963
while first_voting_year <= 2023:
    print(f"Election year: {first_voting_year}")
    first_voting_year+=4

#3
time_oclock = 00
while time_oclock < 24:
    print(f'{time_oclock} oclock')
    time_oclock+=1

#4
months = 1
while months <= 12:
    print(months)
    months+=1
print(f'Total number of months in a year is {months - 1}')