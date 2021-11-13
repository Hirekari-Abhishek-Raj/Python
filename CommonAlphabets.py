alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=int(input())
lst=[]
for i in range(n):
    lst.append(input(""))
for i in alphabets:
    lst1=[]
    for j in lst:
        cnt=j.count(i)
        lst1.append(cnt)
    if 0 not in lst1:
        print(i,min(lst1))
