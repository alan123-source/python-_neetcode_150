class Solution:
    def twosum_pointer(self,numbers:list[int],target: int)->list[int]:
        l,r=0,len(numbers)-1
        while l<r:
            cursum=numbers[l]+numbers[r]
            if cursum > target:
                r-=1
            elif cursum <target:
                l+=1
            else:
                return [l,r]
        return []
sol=Solution()
print(sol.twosum_pointer([1,2,3,4,5,6,7],9))

  #key points to learn from this questions are:
#Whenever you see sorted input + pair/triplet/
# condition checking, always consider the two-pointer
# approach before brute force or hash.


