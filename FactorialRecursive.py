def factorial(n):     
    if n<0:
        return "undefined"
    elif n==0:
        return 1
    else:
        x=factorial(n-1)    
        n=n*x                           
        return n
if __name__ == "__main__":
    n = int(input())
    print(factorial(n)) 
