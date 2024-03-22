#Write a code that will ask the user for their score and will tell them their grade.

x = int(float(input("Enter your score: ")))
if 0>=x and x<=39:
    print("You have F")
elif 40>=x and x<=44:
    print("You have E")
elif 45>=x and x<=49:
    print("You have D")
elif 50>=x and x<=59:
    print("You have C")
elif 60>=x and x<=69:
    print("You have B")
elif 70>=x and x<=100:
    print("You have A")
    print("Well done!")
else:
    print("Invalid score")