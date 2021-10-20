input_string=input("")
N=int(input())
l=len(input_string)
if N==0:
    if l==1:
        print(input_string)
    else:
        X=input_string+input_string[::-1]
        print(X)
elif N==1:
    if l==1:
        print(input_string)
    else:
        X=input_string+input_string[l-2::-1]
        print(X)
