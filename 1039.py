for i in range(int(input())):
    s=input()
    res=s[0:2]
    if  len(s)%2!=0: s += res[1]
    for i in range(int(len(s)/2)-1):
        res+=s[0:2]
    if res==s: print("YES")
    else: print("NO")
    print(res)


