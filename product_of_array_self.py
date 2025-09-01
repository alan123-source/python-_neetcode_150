#ithoinm illa oru integer array thanirikm
# nml return chyun answer enganayiriknm
# equal to product of all the elements
# of that array except that number
# here we use prefix and postfix  refer vedio 6 - 5.10
# thereafter we doesnt use prefix and postfix

class Solution:
    def productExceptSelf(self,nums:list[int])->list[int]:
        res=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

sol=Solution()
print(sol.productExceptSelf([1,2,34,5]))

