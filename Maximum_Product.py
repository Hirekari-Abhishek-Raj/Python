N=int(input())
max= float('-inf')
a=int(input())
for i in range(N-1):
    ele=int(input())
    z=a*ele
    if max<z:
        max=z
    a=ele
print(max)
