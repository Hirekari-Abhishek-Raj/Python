def rec(num):   #num=0
    if num==0:
        return 0
    if num<10:
        return num
    x=num%10    #x=-3%10=-3
    return  x*rec(num//10) #7//10
t=int(input())
for i in range(t):
    num=int(input()) # -31042
    mul=1
    print((rec(abs(num))))
