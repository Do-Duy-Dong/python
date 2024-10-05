n = int(input())
matrix=[[]]*n
sum,sum1=0,0
for i in range(n):
    matrix[i]=list(map(int,input().split()))
y=int(input())
for i in range(n):
    for j in range(i+1,n):
        sum+=matrix[i][j]
    for j in range(0,i):
        sum1+=matrix[i][j]
if abs(sum-sum1)<=y:
    print("YES")
else: print("NO")
print(abs(sum-sum1))