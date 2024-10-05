count =0
b=[]
while count<10:
    a=list(map(int,input().split()))
    count+=len(a)
    for i in a:
        if b.count(i%42)==0:
            b.append(i%42)
print(len(b))
print(a)

