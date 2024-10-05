
def check(n):
    dem=0
    for i in range(len(n)):
        if n[i].isupper():
            dem+=1
        else:
            dem-=1
    if dem<0: print(n.lower())
    else: print(n.upper())
n=input()
check(n)