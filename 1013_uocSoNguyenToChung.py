for i in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    if len(a)==1: print(a[0])
    else:
        dem={}
        cnt,res=1,1
        for j in a:
            if j in dem:
                dem[j]+=1
                if dem[j]>cnt:
                    cnt=dem[j]
                    res=j
            else: dem[j]=1
        if cnt*2>len(a): print(res)
        else: print("NO")




