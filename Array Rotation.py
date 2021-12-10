def rotate_right_K(arr, K):
    K = K % len(arr)
    print(K)
    left = arr[:len(arr) - K]
    right = arr[len(arr) - K:]
    arr = right + left
    print(*arr)
N, Q = [int(i) for i in input().split()]    #N=2,Q=3
num = [int(i) for i in input().split()] #[1,2,3,4,5]
rot = 0     
for _ in range(Q):
    Op, mod = input().split()   #
    mod = int(mod)
    if Op == "R":
        rot += mod
    else:
        rot -= mod
    print(rot)
rotate_right_K(num, rot)
