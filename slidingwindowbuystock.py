class Solution:
    def maxprofit(self,prices:list[int])->int:
        l,r=0,1
        maxp=0
        while r<len(prices):
            if prices[l] <prices[r]:
                profit=prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l+=1
            r+=1
        return maxp
sol=Solution()
print(sol.maxprofit([7,1,5,3,6,4]))

