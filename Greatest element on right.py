def replaceElements(lst):
    # Implement this function
    new_lst=[]
    maxi=lst[-1]
    for i in range(num_elems-2,-1,-1):
        #print(maxi)
        new_lst.append(maxi)
        if lst[i]>maxi:
            maxi=lst[i]
    new_lst=new_lst[::-1]
    new_lst.append(-1)
    return new_lst

# Do not edit anything below
if __name__=="__main__":
    num_elems = int(input())
    arr = []
    for index in range(num_elems):
        arr.append(int(input()))
    
    for elem in replaceElements(arr):
        print(elem)
