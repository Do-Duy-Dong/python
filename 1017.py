for i in range(int(input())):
    s=input()
    dem=0
    tmp=s[0]
    res=""
    for i in s:
        if i!=tmp:
            res += str(dem)
            res+=tmp
            tmp=i
            dem=1
        else: dem+=1
    res+=str(dem)
    res+=s[len(s)-1]
    print(res)