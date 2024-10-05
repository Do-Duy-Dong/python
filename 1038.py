for i in range(int(input())):
    n=input()
    sum = int(n)
    for i in range(1001):
        if sum%7==0:
            print(sum)
            break
        else:
            sum=str(sum)
            sum=int(sum) +int(sum[::-1])
    if sum%7!=0: print("-1")


