N=int(input())
if N>0:
    lst=[]
    countlst=[]
    numlist=[]
    for i in range(N):
        ele=int(input())
        lst.append(ele)
    maxoccur=lst[0]
    count=0
    for i in lst:
        if i==maxoccur:
            count=count+1
        else:
            countlst.append(count)
            numlist.append(maxoccur)
            maxoccur=i
            count=1
    countlst.append(count)
    numlist.append(maxoccur)
    maxcnt=max(countlst)
    for i in range(len(countlst)):
        if maxcnt==countlst[i]:
            print(numlist[i])
else:
    print(-1)
