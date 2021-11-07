n=int(input())
for i in range(n):
    X=input("")
    res="No"
    if len(X)>=5:
        for i in range(0,len(X)-4):
            if X[i]=="h":
                if X[i+1]=="e":
                    if X[i+2]=="l":
                        if X[i+3]=="l":
                            if X[i+4]=="o":
                                res="Yes"
    print(res)
