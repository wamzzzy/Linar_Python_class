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

#small (20naira) coaster type prices for differnt sizes
small20carton = 4000 #contains 65 pieces
medium20carton = 5500 #contains 100 pieces
large20carton = 7000 #contains 140 pieces

both_coaster_type = input('Did you buy the two types of coaster biscuits i.e both the 50naira and 20naira? (Yes or No): ')
if both_coaster_type.upper() == 'YES':
     #Calculation to get total amount for both the 50naira(big) and 20naira (small) type 
     small50 = float(input('How many small cartons of 50naira coaster did you buy(figures only): '))
     medium50 = float(input('How many medium cartons of 50naira coaster did you buy(figures only): '))
     large50 = float(input('How many large cartons of 50naira coaster did you buy(figures only): '))
     total_amount50 = (small50*small50carton)+(medium50*medium50carton)+(large50*large50carton)
     int_total_amount50 = int(total_amount50)
     small20 = float(input('How many small cartons of 20naira coaster did you buy(figures only): '))
     medium20 = float(input('How many medium cartons of 20naira coaster did you buy(figures only): '))
     large20 = float(input('How many large cartons of 20naira coaster did you buy(figures only): '))
     total_amount20 = (small20*small20carton)+(medium20*medium20carton)+(large20*large20carton)
     int_total_amount20 = int(total_amount20)
     total_amount = int_total_amount20+int_total_amount50
     print(f'The total amount to be paid is {total_amount} naira')
     print('Thanks for choosing AM Coaster Biscuits')

elif both_coaster_type.upper() == 'NO':
     #Calculation to get total amount of 50naira (big) coaster type only
     coaster_type = input("Enter the type of coaster biscuits bought\nPlease enter either of the two options as typed in the bracket below\n(50 naira or 20 naira): ")
     if coaster_type.upper() == '50 NAIRA':
          small50 = float(input('How many small cartons of 50naira coaster did you buy(figures only): '))
          medium50 = float(input('How many medium cartons of 50naira coaster did you buy(figures only): '))
          large50 = float(input('How many large cartons of 50naira coaster did you buy(figures only): '))
          total_amount50 = (small50*small50carton)+(medium50*medium50carton)+(large50*large50carton)
          int_total_amount50 = int(total_amount50)
          print(f'The total amount to be paid is {int_total_amount50} naira')
          print('Thanks for choosing AM Coaster Biscuits')

     #Calculation to get total amount of 20naira (small) coaster type only
     elif coaster_type.upper() == '20 NAIRA':
          small20 = float(input('How many small cartons of 20naira coaster did you buy(figures only): '))
          medium20 = float(input('How many medium cartons of 20naira coaster did you buy(figures only): '))
          large20 = float(input('How many large cartons of 20naira coaster did you buy(figures only): '))
          total_amount20 = (small20*small20carton)+(medium20*medium20carton)+(large20*large20carton)
          int_total_amount20 = int(total_amount20)
          print(f'The total amount to be paid is {int_total_amount20} naira')
          print('Thanks for choosing AM Coaster Biscuits')

     else:
          print('Invalid type of coaster biscuits\nPlease enter correct coaster biscuit type')

else:
     print('Invalid option. Please enter correct option')

