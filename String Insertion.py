def stringInsertionSort(str):
    # Your code goes here
    for i in range(1,len(str)):
        key=str[i]
        prev=i-1
        while prev>=0 and key<str[prev]:
            str[prev+1]=str[prev]
            prev=prev-1
        str[prev+1]=key
    return str
### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    lst=[]
    for i in input_string:
        lst.append(i)
    new=""
    for i in stringInsertionSort(lst):
        new=new+i
    print(new)
    
