class Solution:
    def longetsConsecutive(self,nums:list[int])->int:
        num_set=set(nums)
        longest=0
        for n in nums:
            if n-1 not in num_set:
                length=0
                while n+length in num_set:
                    length+=1
                longest=max(length,longest)
        return longest
sol=Solution()
print(sol.longetsConsecutive([1,2,3,4,100,101,102,103,104]))

# 🔹 Key Concepts / Patterns from this Problem
#
# Hashing for Fast Lookups""
#
# Using a hash set allows O(1) average-time membership checks.
#
# Pattern: when you need to check existence quickly in an array, consider a hash set.
#
# Finding Sequence Starts
#
# Instead of checking every number in the array, only start counting from the beginning of a sequence:
#
# if n-1 not in num_set
#
#
# Pattern: when detecting consecutive elements, identify a “start point” to avoid redundant work.
#
# Sliding / Counting Forward
#
# Use a loop to walk forward from the start until the sequence ends:
#
# while n + length in num_set:
#     length += 1
#
#
# Pattern: iteratively expand a sequence until a condition fails.
#
# Optimizing Time Complexity
#
# Naive approach (sorting + counting) = O(n log n)
#
# Hashing approach = O(n)
#
# Pattern: use extra space (hash set) to reduce time in linear-time problems.
#
# Handling Unordered Data
#
# The array is unsorted, yet we still detect sequences efficiently.
#
# Pattern: unordered data + sequence detection → hashing.
#
# Edge Cases to Remember
#
# Empty array → return 0
#
# Single element → return 1
#
# Duplicates → hash set automatically handles them