#using for loop to get multiplication table

for fnum in range (1,13):
    for snum in range (1,13):
        answer =  fnum*snum
        print(f'{fnum}*{snum} = {answer}')
    print('\n\n')