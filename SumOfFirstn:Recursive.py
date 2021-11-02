def sumOfFirstN(n):
    # Implement this function
    if n==1:
        print(1,1)
        return 1
    else:
        s=n + sumOfFirstN(n-1)
        print(n,s)
        return s

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)
