#solving for Y

f = int(float(input("f = ")))
L = int(float(input("L = ")))
n = int(float(input("n = ")))
s = int(float(input("s = ")))
w = int(float(input("w = ")))
f_n = f**n
termA_one = (s*L)/f
termA_two = (20/f)**w
num = f_n*(termA_one+termA_two)
termB_one = 20**n
termB_two = (9**(1/3))/(w**(f/2))
den = termB_one+f_n+termB_two
Y = L-(num/den)
print("Y = "+str(int(Y)))