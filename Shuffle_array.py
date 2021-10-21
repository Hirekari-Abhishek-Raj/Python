def shuffle(arr):
    # Implement this function
    i=0
    j=n
    lst=[]
    while j<(2*n):
        lst.append(arr[i])
        lst.append(arr[j])
        i+=1
        j+=1
    return lst

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)
