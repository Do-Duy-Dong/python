t=int(input())
for i in range(t):
    res=""
    tmp=[]
    s=input()
    s+="?"
    for j in range(len(s)):
        if s[j].isdigit():
            res+=s[j]
        elif res!="" :
          tmp.append(int(res))
          res=""
    print(min(tmp))