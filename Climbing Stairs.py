class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def climb(n):     #n=1
            if n==1:
                return 1
            if n==2:
                return 2
            if n in d:
                return d[n]
            x=climb(n-1)  #x=2
            y=climb(n-2)  #y=1
            d[n]=x+y
            return x+y  #x+y=3
        return climb(n)   #n=3
