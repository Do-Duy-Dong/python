import math
for i in range(int(input())):
    a=int(input())
    print("1",end="")
    for j in range(2,math.isqrt(a),1):
            dem=0
            while a%j==0:
                a/=j
                dem+=1
            if dem!=0:print(f" * {j}^{dem}",end="")
    if a!=1: print(f" * {int(a)}^1",end="")
    print()

