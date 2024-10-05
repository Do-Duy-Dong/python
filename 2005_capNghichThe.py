n=int(input())
dem=0
a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]: dem+=1
print(dem)
#2 4 1 3 5
