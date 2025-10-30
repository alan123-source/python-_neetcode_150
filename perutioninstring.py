class Solution:
    def permutaioninstring(self,s1:str,s2:str)->bool:
        if len(s1)>len(s2):
            return False
        s1count,s2count=[0]*26,[0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord("a")]+=1
            s2count[ord(s2[i]) - ord("a")] += 1

        matches=0
        for i in range(26):
            if s1count[i]==s2count[i]:
                matches+=1
            else:
                matches+=0
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord("a")
            s2count[index]+=1
            if s1count[index]==s2count[index]:
                matches+=1
            elif s1count[index]+1==s2count[index]:
                matches-=1
            index = ord(s2[l]) - ord("a")
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l+=1
        return matches==26
sol=Solution()
print(sol.permutaioninstring())
# 1. Sliding Window
#
# Instead of checking all substrings of length len(s1) (which would be O(n*m)), we keep a fixed-size window of len(s1) and just slide it across s2.
#
# Window size is constant → len(s1).
#
# Each step only adds 1 character (right) and removes 1 character (left).
# 👉 Key Pattern: When searching for substrings of fixed length, use sliding window.
#
# 2. Frequency Counting (Array instead of Hash Table)
#
# We need to know if two substrings have the same characters (just permuted).
#
# Instead of sorting (which would be O(m log m)), we compare frequency counts of letters.
#
# Because only lowercase English letters are used, we can use a 26-size array ([0]*26) instead of a dictionary.
# 👉 Key Pattern: Use fixed-size frequency arrays for character counts when input domain is small (like lowercase letters).
#
# 3. Efficient Match Tracking
#
# Naively, you could compare two frequency arrays at every step → O(26) per step.
#
# But here, the trick is to keep a running matches counter (how many characters match between the two windows).
#
# So instead of checking full arrays every time, you only update matches when one character is added/removed.
# 👉 Key Pattern: Keep a running metric (matches) to avoid re-comparing entire structures each step.
#
# 4. Fixed-Window vs Variable-Window
#
# This problem is fixed window (always size len(s1)), unlike some substring problems where you expand and shrink dynamically (longest substring without repeating, etc).
# 👉 Key Pattern: Decide early whether the sliding window size is fixed or variable.
#
# 5. Permutation Check via Character Counts
#
# A permutation of a string has the same character frequency as the original string.
#
# So, instead of generating permutations (which is exponential), just compare counts.
# 👉 Key Pattern: Many permutation-related problems reduce to comparing frequency counts.




