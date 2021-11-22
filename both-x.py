def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    string1=string1.lower()
    string2=string2.lower()
    lst=[]
    if len(string1)<=len(string2):
        for i in string1:
            if i not in lst:
                new1=string1.count(i)
                new2=string2.count(i)
                if new1==new2==x :
                    lst.append(i)
    else:
        for i in string2:
            if i not in lst:
                new1=string1.count(i)
                new2=string2.count(i)
                if new1==new2==x :
                    lst.append(i)
        
    lst.sort()
    return lst
for i in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))
