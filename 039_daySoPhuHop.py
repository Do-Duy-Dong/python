t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    check=True
    for i in range(n):
        if b[i]<a[i]:
            print("NO")
            check=False
            break
    if check==True: print("YES")

