n=int(input())
sum=0
for i in range(n):
    sum=sum+int(input())
print(sum//n)
if sum//n<25:
    print("True")
else:
    print("False")
