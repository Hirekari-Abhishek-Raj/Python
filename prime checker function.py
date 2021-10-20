def is_prime(input_number):
    count=0
    for i in range(1,input_number+1):
        p=input_number%i
        if p==0:
            count=count+1
    if count==2:
        return True
    else:
        return False
        
if __name__ == "__main__":
    number = int(input())
    print(is_prime(number))
