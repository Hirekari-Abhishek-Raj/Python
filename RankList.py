big_list=[]
for i in range(int(input())):
    name,scholar,marks=input().split()
    lst=[name,int(scholar),int(marks)]
    big_list.append(lst)
big_list.sort(key=lambda x:(x[0],x[1]))
big_list.sort(key=lambda x:x[2],reverse=True)
for i in big_list:
    print(*i)
