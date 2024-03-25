#Develop a software that helps calculate the total amount of coaster carton a customer order in your coaster biscuit depot office.
#where you only sell coaster biscuits and only sell in bulks(only carton and half carton)
#where there two types of coaster biscuits available, the 50naira(Big type) and the 20naira(Small type)
#The software will ask what type of coaster is bought, carton quantity bought, what size(small, medium, large) is bought and then calculates the toatl amount to be paid.
#with the prices of each carton sizes for both 50naira and 20naira given


print('Hello!\nWelcome to AM Coaster Biscuits')

#big (50naira) coaster type prices for differnt sizes
small50carton  = 4000 #contains 45 pieces
medium50carton = 5500 #contains 75 pieces
large50carton = 7000 #contains 110 pieces
half_small50carton = small50carton/2 #contains half of 45 pieces
half_medium50carton = medium50carton/2 #contains half of 75 pieces
half_large50carton = large50carton/2 #contains half of 110 pieces

#small (20naira) coaster type prices for differnt sizes
small20carton = 4000 #contains 65 pieces
medium20carton = 5500 #contains 100 pieces
large20carton = 7000 #contains 140 pieces
half_small20carton = small20carton/2 #contains half of 65 pieces
half_medium20carton = medium20carton/2 #contains half of 100 pieces
half_large20carton = large20carton/2 #contains half of 140 pieces

#Calculation to get total amount of 50naira (big) coaster type
coaster_type = input('Enter the type of coaster biscuits bought (50naira or 20naira): ')
if coaster_type.upper() == '50NAIRA':
    small50 = int(input('How many small full cartons of 50naira coaster did you buy(figures only): '))
    half_small50 = int(input('How many small half cartons of 50naira coaster did you buy(figures only): '))
    medium50 = int(input('How many medium full cartons of 50naira coaster did you buy(figures only): '))
    half_medium50 = int(input('How many medium half cartons of 50naira coaster did you buy(figures only): '))
    large50 = int(input('How many large full cartons of 50naira coaster did you buy(figures only): '))
    half_large50 = int(input('How many large half cartons of 50naira coaster did you buy(figures only): '))
    total_amount50 = (small50*small50carton)+(medium50*medium50carton)+(large50*large50carton)+(half_small50*half_small50carton)+(half_medium50*half_medium50carton)+(half_large50*half_large50carton)
    int_total_amount50 = int(total_amount50)
    print(f'The total amount to be paid is {int_total_amount50} naira')

#Calculation to get total amount of 20naira (small) coaster type
elif coaster_type.upper() == '20NAIRA':
     small20 = int(input('How many small full cartons of 20naira coaster did you buy(figures only): '))
     half_small20 = int(input('How many small half cartons of 20naira coaster did you buy(figures only): '))
     medium20 = int(input('How many medium full cartons of 20naira coaster did you buy(figures only): '))
     half_medium20 = int(input('How many medium half cartons of 20naira coaster did you buy(figures only): '))
     large20 = int(input('How many large full cartons of 20naira coaster did you buy(figures only): '))
     half_large20 = int(input('How many large half cartons of 20naira coaster did you buy(figures only): '))
     total_amount20 = (small20*small20carton)+(medium20*medium20carton)+(large20*large20carton)+(half_small20*half_small20carton)+(half_medium20*half_medium20carton)+(half_large20*half_large20carton)
     int_total_amount20 = int(total_amount20)
     print(f'The total amount to be paid is {int_total_amount20} naira')

else:
     print('Invalid type of coaster biscuits\nPlease enter correct coaster biscuit type')


