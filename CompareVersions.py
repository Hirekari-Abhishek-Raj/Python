def comp(lst1,lst2):
    for i in range(min(len(lst1),len(lst2))):
        if lst1[i]>lst2[i]:
            return 1
        elif lst1[i]<lst2[i]:
            return -1
    if len(lst1)>len(lst2):
        for i in range(len(lst2),len(lst1)):
            if lst1[i]>0:
                return 1
    if len(lst2)>len(lst1):
        for i in range(len(lst1),len(lst2)):
            if lst2[i]>0:
                return -1
    return 0
        
for i in range(int(input())):
    lst=[i for i in input().split()]
    lst1=[int(i)for i in lst[0].split(".")]
    lst2=[int(i)for i in lst[1].split(".")]
    print(comp(lst1,lst2))
