class Solution:
    def twosum(self,nums: list[int],target: int) -> list[int]:
        prevMap={} #val:index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i#adds current number and index to the hashmap
        return []
sol=Solution()
print(sol.twosum([2,1,5,3],8))

# ithenagan work chyuneen vechal numsinakath poi
# indexm value nokm  ath kazhinj diff calculate chym
# athenthan vechal oru numberinte koode vere oru number matram
# add chythale  aa target kitoloo
# so aa number matram kand pidichal mathy apm
# diff nokum nokit ath prevmap hash
# tabilil ondon nokm  nokiyt illenkil ath add
# chym athava ondenkil aa  key valuem cuurnt valem return akm
