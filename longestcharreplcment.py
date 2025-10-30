class Solution:
    def charreplacement(self,s:str,k:int)->int:
        l=0
        res=0
        count={}
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1)-max(count.values()) >k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
sol=Solution()
print(sol.charreplacement("ABAB",2))

# 🔑 Key Patterns to Remember
# 1. Sliding Window
#
# You always use two pointers l and r.
#
# Expand r to include new characters.
#
# Shrink l only when the condition is violated.
#
# 2. Character Frequency Map
#
# Use a hashmap (count) to track frequency of characters in the current window.
#
# This tells you how many of each character you have inside the window.
#
# 3. Valid Window Condition
#
# Window length = (r - l + 1)
#
# Max frequency of a single character = max(count.values())
#
# If (window size - max frequency) <= k → ✅ window is valid.
#
# Else → shrink window by moving l.