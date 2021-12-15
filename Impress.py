from sys import stdin,stdout
def Which_Day(a, x):
    start, end = 0, len(a)-1
    while(start <= end):
        mid = (start+end)//2
        if a[mid] >= x:
            res = mid
            end = mid-1
        else:
            start = mid+1
    return res
n,q = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
for i in range(n):
    if i!=0:
        a[i] = a[i-1]+a[i]
k = list(map(int,stdin.readline().split()))
for i in range(q):
    ans = Which_Day(a,k[i])+1
    stdout.write(str(ans)+"\n")
