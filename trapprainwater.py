class Solution:
    def rainwatertrap(self,heights:list[int])->int:
        l,r=0,len(heights)-1
        res=0
        leftmax,rightmax=heights[l],heights[r]
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,heights[l])
                res+=leftmax-heights[l]
            else:
                r-=1
                rightmax=max(rightmax,heights[r])
                res+=rightmax-heights[r]
        return res
sol=Solution()
print(sol.rainwatertrap([0,1,0,2,1,0,1,3,2,1,2,1]))
