def inc(lst1):
    lst2=[]
    while lst1:
        min = lst1[0]  
        for i in lst1: 
            if i < min:
                min = i
        lst2.append(min)
        lst1.remove(min)
    return lst2
def dec(lst1):
    lst2=[]
    while lst1:
        max = lst1[0]  
        for i in lst1: 
            if i > max:
                max = i
        lst2.append(max)
        lst1.remove(max)
    return lst2
n=int(input())
for i in range(n):
    lst=[]
    evelst=[]
    oddlst=[]
    lst=[int(i)for i in input().split()]
    for i in range(len(lst)):
        if i%2==0:
            evelst.append(lst[i])
        else:
            oddlst.append(lst[i])
    evelst=dec(evelst)
    oddlst=inc(oddlst)
    newlst=[]
    if len(lst)%2==0:
        for i in range(len(lst)//2):
            newlst.append(evelst[i])
            newlst.append(oddlst[i])
    else:
        for i in range(len(lst)//2):
            newlst.append(evelst[i])
            newlst.append(oddlst[i])
        newlst.append(evelst[-1])
    for i in newlst:
        print(i,end=" ")
