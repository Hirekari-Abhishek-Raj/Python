n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
m=lst[0]
for i in range(n):
    if i==0:
        print(lst[i])
    else:
        x=max(lst[i],m)
        m=x
        print(m)
    
