#num ,skills,minAssociates,minLevel,maxLevel
num=int(input())
skills=[int(i)for i in input().split()]
minAssociates=int(input())
minLevel=int(input())
maxLevel=int(input())
lst=[]
import math
def combination(n,r):
    x=math.factorial(n)//((math.factorial(r))*(math.factorial(n-r)))
    print(x)
    return x
for i in skills:
    if i>=minLevel and i<=maxLevel:
        lst.append(i)
print(lst)
print(minAssociates)
if minAssociates>len(lst):
    
    print(0)
else:
    summ=0
    for i in range(minAssociates,len(lst)+1):
        summ+=combination(len(lst),i)
    print(summ)
    
