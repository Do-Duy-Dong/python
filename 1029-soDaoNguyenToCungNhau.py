import math
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)
for i in range(int(input())):
    n=input()
    n1=n[::-1]
    if gcd(int(n),int(n1))==1: print("YES")
    else: print("NO")
