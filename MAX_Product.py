n=int(input())
N=int(input())
A=[abs(int(i))for i in input().split()]
B=[abs(int(i))for i in input().split()]
print(max(A)*max(B))
