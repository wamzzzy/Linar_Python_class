print("Hello!")
name = input("Enter your name: ")
print("Welcome "+str(name))
x = int(float(input("Enter your age: ")))
if x>=0 and x<=2:
    print("You are an infant, "+str(name))
elif x>=3 and x<=12:
    print("You are a beautiful kid, "+str(name))
elif x>=13 and x<=19:
    print("You are a teenager, "+str(name))
elif x>=20 and x<=29:
    print("You are in your youth age, "+str(name))
elif x>=30 and x<=49:
    print("You are a Wonderful young adult, "+str(name))
elif x>=50 and x<=60:
    print("You are an Adult, "+str(name))
elif x>=61 and x<=99:
    print("You are an Old adult, "+str(name))
else:
    print("Invalid age")