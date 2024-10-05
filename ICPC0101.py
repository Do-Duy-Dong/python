n=int(input())
a=list(map(int,input().split()))
b=[]
dem=1
for i in range(len(a)):
        b.append(a[i]%42)
for i in range(len(b)):
    if b.count(b[i])==1:
        dem+=1

print(dem)