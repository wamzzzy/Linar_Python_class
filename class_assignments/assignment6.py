#solving for S

a = int(input("a = "))
d = int(input("d = "))
n = int(input("n = "))
termN = n/2
termB = (2*a)+((n-1)*d)
S = termN*termB
print("S = "+str(int(S)))