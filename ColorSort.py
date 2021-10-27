n=int(input())
Red=0
White=0
Blue=0
for i in range(n):
    x=int(input())
    if x==0:
        Red+=1
    elif x==1:
        White+=1
    else:
        Blue+=1
for i in range(Red):
    print(0)
for i in range(White):
    print(1)
for i in range(Blue):
    print(2)
