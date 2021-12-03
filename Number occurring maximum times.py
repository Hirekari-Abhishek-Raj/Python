dict={}
flag=0
n=int(input())
for i in range(n):
    val=int(input())
    if val not in dict:
        dict[val]=1
    else:
        dict[val]+=1
for i in dict.keys():
    if dict[i]==4:
        print(i)
        flag=1
if flag==0:
    print(-1)
