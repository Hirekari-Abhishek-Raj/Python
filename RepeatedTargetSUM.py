def rec(i,pat,res,rem):
    if (rem==0 and i==len(lst)):
        if pat not in res:
            res.append(pat)
        return
    elif rem<0 or i==len(lst):
        return
    rec(i,pat+[lst[i]],res,rem-lst[i])
    rec(i+1,pat+[lst[i]],res,rem-lst[i])
    rec(i+1,pat,res,rem)
n,target=map(int,input().split())
lst=[int(i)for i in input().split()]
pat=[]
res=[]
rec(0,pat,res,target)
print(len(res))
