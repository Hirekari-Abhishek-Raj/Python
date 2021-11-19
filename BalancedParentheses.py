def getAllBalancedParan(s,Open,Close,n,arr):
    if Open==n and Close==n:
        arr.append(s)
        return arr
    if Open<n:
        getAllBalancedParan(s+'(',Open+1,Close,n,arr)
    if Close<Open:
        getAllBalancedParan(s+')',Open,Close+1,n,arr)
    return arr

# Do not edit anything below
n = int(input())
arr=[]
allBalancedParan = getAllBalancedParan('',0,0,n,arr)
allBalancedParan.sort()
for expr in allBalancedParan:
    print(expr)
