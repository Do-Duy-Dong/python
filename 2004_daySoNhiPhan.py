dem=0
n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        dem+=1
print(dem)