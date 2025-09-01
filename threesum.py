class Solution:
    def threesum(self,nums:list[int])->list[list[int]]:
        nums.sort()
        output=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
            return output
sol=Solution()
print(sol.threesum([-3,3,4,-3,1,2]))






