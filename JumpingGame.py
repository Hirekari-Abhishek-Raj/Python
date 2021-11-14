def jump(i,jp):
    if i>=n:
        jmp.append(jp)
        return
    jump(i+1,jp+1)
    jump(i+lst[i],jp+1)
    return jmp
n=int(input())
lst=[int(i)for i in input().split()]
jmp=[]
jump(0,0)
print(min(jmp))
