def pivotIndex(arr):
    left=0
    right=sum(arr)
    for i in range(num_elems):
        right-=arr[i]
        if right==left:
            return i
        left+=arr[i]
    return -1

# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))
