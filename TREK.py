for i in range(int(input())):
    n=int(input())
    string=input()
    step=0
    valley=0
    prev=0
    for i in range(n):
        if string[i]=="D":
           step-=1
           
        else:
            step+=1
        if step==-1 and prev ==0:
            valley+=1
        prev=step
    print(valley)
