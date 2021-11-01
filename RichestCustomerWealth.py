class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=float("-inf")
        for i in range(len(accounts)):
            x=sum(accounts[i])
            if x>m:
                m=x
        return m
