a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
r = ((b**2)-(4*a*c))**0.5
d = 2*a
x_one = ((-b)+r)/d
x_two = ((-b)-r)/d
print("x = "+str(int(x_one))+(" or x = "+str(int(x_two))))