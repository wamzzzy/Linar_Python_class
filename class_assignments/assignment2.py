#calculator for quadratic formula

A=input("a = ")
B=input("b = ")
C=input("c = ")
termb1=int(B)**2
termb2=4*int(A)*int(C)
termb3=termb1-termb2
termb=termb3**0.5#solving the square root
num1=-int(B)+termb#numerator for the addition operator
num2=-int(B)-termb#numerator for the subraction operator
den=2*int(A)#denumenator
x1=num1/den
x2=num2/den
print("x1 = "+str(int(x1)))
print("x2 = "+str(int(x2)))