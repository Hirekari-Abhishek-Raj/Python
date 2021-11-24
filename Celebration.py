t=int(input())
for i in range(t):
    maxx=0
    dict={}
    n=int(input())
    for i in range(n):
    	x,y=input().split()
    	S=(x,y)
    	if S not in dict:
    		dict[S]=1
    	else:
    		dict[S]+=1
    if n>0:
        maxx=max(dict.values())
    print(maxx)
