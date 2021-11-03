def rev(s,y):
    if y==0:
        return ""
    return s[y-1]+rev(s,y-1)
n=int(input())
for i in range(n):
    x=input("")
    y=len(x)
    print(rev(x,y))
