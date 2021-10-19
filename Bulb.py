# your code goes here
N=int(input())
count=0
change=0
for i in range(N):
    switch=input("")
    if switch=='ON':
        if change==0:
            count+=1
        change=1
    elif switch=='OFF':
        change=0
    elif switch=='Toggle':
            if change==0:
                count+=1
                change=1
            else:
                change=0
print(count)
