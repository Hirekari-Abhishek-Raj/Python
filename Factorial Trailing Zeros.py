def trailingZeroes(n):
    # WRITE YOUR CODE HERE
    count=0
    while n>=5:
        n=n//5
        count +=n
    return count
# DO NOT CHANGE ANYTHING BELOW THIS LINE
num_tests=int(input())
for _ in range(num_tests):
    n=int(input())
    print(trailingZeroes(n))
