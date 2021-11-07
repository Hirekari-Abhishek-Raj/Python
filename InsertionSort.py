def insertionSort(A, n):            
    for index in range(1,n):        
        key=A[index]                #key=2 index=2
        prev_index=index-1          #prev=1
        while prev_index<=0 and key<A[prev_index]:
            A[prev_index+1]=A[prev_index]
            prev_index=prev_index-1
        A[prev_index+1]=key
    return A

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()] #5 10 2 4 -12
        print(*insertionSort(arr, n))
