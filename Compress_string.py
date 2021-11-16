def compress(st):
    count=1
    string=''
    if len(st)==1 or len(st)==0:
    	print(st)
    	return
    for i in range(1,len(st)):
        if st[i]==st[i-1]:
            count+=1
        else:
            string=string+st[i-1]
            if count>1:
                string=string+str(count)
            count=1
    if len(st)>=2 and st[-2]==st[-1]:
        string=string+st[-2]
        if count>1:
            string=string+str(count)
    if len(st)>=2 and st[-2]!=st[-1] and i==len(st)-1:
            string=string+st[i]
    print(string)

t = int(input())
for i in range(t):
    st = input()
    compress(st)
