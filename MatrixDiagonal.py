def change_diagonal(lst):
    for i in range(val):
        if lst[i][i]<0:
           lst[i][i]=0
        else:
            lst[i][i]=1
    return lst

if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))
