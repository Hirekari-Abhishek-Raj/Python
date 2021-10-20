# your code goes here
N=int(input())
image=[]
for i in range(N):
    ele=int(input())
    image.append(ele)
icon=[]
n=int(input())
for i in range(n):
    p=int(input())
    icon.append(p)
count=0
if n==0:
    print(0)
elif n==1:
    x=image.count(icon[0])
    print(x)
else:
    for i in range(1,N):
        if icon[0]==image[i-1] and icon[1]==image[i]:
            count=count+1
    print(count)
