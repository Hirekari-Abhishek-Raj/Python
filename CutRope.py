def cutRope(A):
    # Complete this function
    
    new_A=[]
    x=min(A)
    for i in A:
        if i-x!=0:
            
            new_A.append(i-x)
    
    if len(new_A)==0:
        return
    lst.append(len(new_A))
    cutRope(new_A)
    return lst
	
# Do not change anything below this line
if __name__ == '__main__':
    input_numbers = []
    lst=[]
    for _ in range(int(input())):
        input_numbers.append(int(input()))

    for i in cutRope(input_numbers):
        print(i)
