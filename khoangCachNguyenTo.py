import math
def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i==0: return False
    return True
a,b=map(int,input().split())
i=2
list=[]
while(len(list)<=1001):
    if snt(i)==True:
        list.append(i)
    i+=1
print(b,end=" ")
for i in range(a):
    b+=list[i]
    print(b,end=" ")