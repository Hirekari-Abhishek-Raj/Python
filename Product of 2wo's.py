n=int(input())
lst=[abs(int(i))for i in input().split()]
total_sum=sum(lst)
summ=0
ti=0
for i in lst:
    ti=ti+i
    summ=summ+i*(total_sum-ti)
    # print(ti)
print(summ)
