def transpose_matrix(lst):
    t=[]
    for i in range(len(lst[0])):
        x=[]
        for j in range(len(lst)):
           x.append(lst[j][i])
        t.append(x)
    return t
if __name__ == "__main__":
    h = int(input())
    lst = []
    for val in range(0, h):
        lst.append([int(i) for i in input().split(' ')])
    out = transpose_matrix(lst)
    for val in out:
        print(" ".join(str(i) for i in val))
