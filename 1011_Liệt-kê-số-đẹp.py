n=int(input())
def chiaHetCho2(s):
    s=str(s)
    if len(s)%2==1: return False
    for i in s:
        if int(i)%2==1: return False
    return True

def soThuanNghich(s):
    s1=str(s)
    for i in range(0,int(len(s1)/2),1):
        if s1[i]!=s1[len(s1)-i-1]:
            return False
    return True

for i in range(n):
    s=input()
    for j in range(22,int(s),2):
        if chiaHetCho2(j)==True and soThuanNghich(j)==True:
            print(j)
