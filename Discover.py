def find_k(l, k):
    # Implement this and return YES if found else return No
    if k in l:
        return "YES"
    return "NO"
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
lst=set()
a.sort()
for i in a:
    lst.add(i)
for i in range(int(Q)):
    k = int(input())
    print(find_k(lst, k))
