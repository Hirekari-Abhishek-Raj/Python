for i in range(int(input())):
    string=input("")
    count=0
    n=len(string)
    start=0
    end=n-1
    res=False
    for i in range(n//2):
        if string[start]==string[end]:
            res=True
        else:
            if string[start+1]==string[end] and count==0:
                res=True
                start=start+1
                count=1
            elif string[start]==string[end-1] and count==0:
                res=True
                end=end-1
                count=1
            else:
                res=False
                break
        start=start+1
        end=end-1

    print(res)
