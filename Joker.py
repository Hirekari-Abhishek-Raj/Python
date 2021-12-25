A=[int(i)for i in input().split()]           
lst=[A[-1]]
max_num=A[-1]
for i in range(len(A)-2,-1,-1):
    if A[i]>max_num:
        lst.append(A[i])
        max_num=A[i]
print(lst)
