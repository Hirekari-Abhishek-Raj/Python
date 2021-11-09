def table(x,i):
    if i==11:
        return
    lst.append(x*i)
    i=i+1
    table(x,i)
    return lst
x=int(input())
lst=[]
print(" ".join(str(i)for i in table(x,1)))
