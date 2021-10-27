r,c=input().split()
r,c=int(r),int(c)
lst=[]
new=[]
for i in range(r):
    lst.append([int(j)for j in input().split()])
left,right,top,bottom=input().split()
left,right,top,bottom=int(left),int(right),int(top),int(bottom)
for i in range(top-1,bottom):
    temp=[]
    for j in range(left-1,right):
        temp.append(lst[i][j])
    new.append(temp)
for i in new:
    print(" ".join(str(j)for j in i))
