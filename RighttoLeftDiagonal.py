
def right_to_left_diagonal(lst):
    di=[]
    j=m-1
    for i in range(m):
        di.append(lst[i][j])
        j-=1
    return di


# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]
