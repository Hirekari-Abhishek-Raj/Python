n=int(input())
lst=[int(i)for i in input().split()]
dict={}
for i in lst:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
maxx=float("-inf")
for i in dict:
    if dict[i]>maxx:
        maxx=dict[i]
        lst=[i]
    elif dict[i]==maxx:
        lst.append(i)
print(min(lst))
    
