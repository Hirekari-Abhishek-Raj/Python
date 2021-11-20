def peace(s,i,n):
    if i==n:
        lst.append(s)
        return
    if i<=1 :
        peace(s+'a',i+1,n)
        peace(s+'b',i+1,n)
    if i>1 and s[-1]!=s[-2]:
        peace(s+'a',i+1,n)
        peace(s+'b',i+1,n)
    if i>1 and s[-1]==s[-2]=='a':
        peace(s+'b',i+1,n)
    if i>1 and s[-1]==s[-2]=='b':
        peace(s+'a',i+1,n)
    return
n=int(input())
lst=[]
peace('',0,n)
for i in lst:
    print(i)
