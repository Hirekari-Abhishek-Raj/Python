def findLuckyNumber(nums):
    # implement this function
    n=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            n=n+1
        else:
            if n==nums[i-1]:
                return nums[i-1]
            else:
                n=1
    if n==nums[-1]:
        return nums[-1]
    return -1


if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
