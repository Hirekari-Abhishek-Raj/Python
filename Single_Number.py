
N=int(input())
lst=[]
for i in range(N):
    ele=int(input())
    lst.append(ele)
for i in lst:
    if lst.count(i)==1:
        print(i)
