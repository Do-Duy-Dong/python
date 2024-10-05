for i in range(int(input())):
    s=input()
    res=""
    for i in range(0,len(s),1):
        if i%2==1:
            for j in range(0,int(s[i]),1):
                res+=s[i-1]
    print(res)
