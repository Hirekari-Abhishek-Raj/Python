def binomialCoeff(n, r):
    # Implement this function
    if r==0 or n==r:
        return 1
    else:
        z= binomialCoeff(n-1,r-1)+binomialCoeff(n-1,r)
        return z

# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))
