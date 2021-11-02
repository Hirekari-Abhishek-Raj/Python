def gcd(dividend, divisor):
    # Implement this function
    if dividend%divisor==0:
    	return divisor
    return gcd(divisor,dividend%divisor)

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    for index in range(n):
        inputInts = input().split(' ')
        dividend = int(inputInts[0])
        divisor = int(inputInts[1])
        print(gcd(dividend, divisor))
