n=int(input())
for i in range(n):
    s=input()
    if s[:2]==s[len(s)-2:]:
        print("YES")
    else: print("NO")