# your code goes here
n=int(input())
i=1
j=1
while(i<=n):
    j=1
    print(" "*(n-i),end="")
    while(j<=(2*i)-1):
        if i%2!=0:
            if j%2!=0:
                print("*",end="")
            else:
                print("$",end="")
        else:
            if j%2!=0:
                print("$",end="")
            else:
                print("*",end="")
        j=j+1
    print("")
    i=i+1
