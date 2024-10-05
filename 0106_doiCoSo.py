def transfer(s):
    tong=0
    for i in range(len(s)):
        if int(s[i])==1: tong+=pow(2,i)

    return tong
n=int(input())
for i in range(n):
    para=int(input())
    dem=1
    while para!=2:
        para/=2
        dem+=1
    s=input()
    res=""
    while len(s)%dem!=0:
        s="0"+s
    for i in range(len(s),0,-dem):
        sub=s[i-dem:i]
        res+=str(transfer(sub[::-1]))
    print(res[::-1].upper())




