import math
for i in range(int(input())):
    tong=0
    n=int(input())
    for i in range(1,n+1,2):
        if n%2==0: tong+=1/(i+1)
        else: tong+=1/i
    print(f"{tong:.6f}")