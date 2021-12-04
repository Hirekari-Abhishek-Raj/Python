t = int(input())
for i in range(t):
    girls = int(input())
    arr = []
    for j in range(girls):
        arr.append([int(x) for x in input().split()])
    arr.sort(key=lambda x: x[0]+x[1], reverse=True)
    unhappy = 0
    for i in range(girls):
        unhappy += arr[i][1]
    total = arr[0][0]+arr[1][0]+arr[0][1]+arr[1][1]
    print(total-unhappy)
