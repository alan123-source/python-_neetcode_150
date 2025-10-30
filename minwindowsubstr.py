from itertools import count

# class Solution:
#      def minwin(self,s:str,t:str)->str:
#          if t=="":
#              return ""
#          window,countT={},{}
#          for c in t:
#              countT[c]=1+countT.get(c,0)
#
#          have,need=0,len(countT)
#          res,reslen=[-1,-1],float("infinity")
#          l=0
#          for r in range(len(s)):
#
#              c=s[r]
#              window[c]=1+window.get(c,0)
#              if c in countT and window[c]==countT[c]:
#                  have+=1
#              while have==need:
#                  if (r-l+1) <reslen:
#                      res=[l,r]
#                      reslen=(r-l+1)
#                  window[s[l]]-=1
#                  if s[l] in countT and window[s[l]] < countT[s[l]]:
#                      have-=1
#                  l+=1
#          l,r=res
#          if reslen!=float("infinity"):
#              return s[l:r+1]
#          else:
#             return ""

class solution:
    def minwindowsubstring(self,s:str,t:str)->str:
        if t=="":
            return False

        windows,countT={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        have,need=0,len(countT)
        res,reslen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            windows[c]=1+windows.get(c,0)
            if c in countT and windows[c]==countT[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=(r-l+1)
                windows[s[l]]-=1
                if s[l] in countT and windows[s[l]]<countT[s[l]]:
                    have-=1
                l+=1







# I'll show each time we expand (move r and add s[r]) and each time we shrink (the while have == need loop). For brevity I list counts only for A, B, C (others are present but not required).
#
# r=0, add 'A'
#
# window: A=1, B=0, C=0
#
# A reached required count → have = 1 (not yet need)
#
# no shrink.
#
# r=1, add 'D'
#
# window: A=1, B=0, C=0 (D is present but not required)
#
# have = 1 → no shrink.
#
# r=2, add 'O'
#
# window unchanged for A/B/C → have = 1.
#
# r=3, add 'B'
#
# window: A=1, B=1, C=0
#
# B reached required → have = 2.
#
# r=4, add 'E'
#
# window unchanged for A/B/C → have = 2.
#
# r=5, add 'C'
#
# window: A=1, B=1, C=1 → have = 3 == need → window [l=0 .. r=5] is VALID
#
# Current length = 6. Update best: res = [0,5], reslen = 6.
#
# Now shrink from left:
#
# remove s[0]='A' → A becomes 0 (below required) → have decrements to 2, l becomes 1.
#
# Because have < need, stop shrinking.
#
# r=6, add 'O' → have = 2.
#
# r=7, add 'D' → have = 2.
#
# r=8, add 'E' → have = 2.
#
# r=9, add 'B'
#
# window B increases (now maybe >1) but it does not change have because have only counts when a char reaches exactly the required count the first time. → have = 2.
#
# r=10, add 'A'
#
# window: now A=1, B>=1, C=1 → A reached required again → have = 3 == need → window [l=1 .. r=10] is VALID
#
# Current length = 10 (not smaller than 6), so we will try to shrink to find smaller valid windows:
#
# shrink s[1]='D' → D not required → have = 3, l=2
#
# shrink s[2]='O' → not required → have = 3, l=3
#
# shrink s[3]='B' → B goes from 2 → 1 (still ≥ required) → have = 3, l=4
#
# shrink s[4]='E' → not required → have = 3, l=5
#
# shrink s[5]='C' → C becomes 0 (below required) → have becomes 2, l=6 → stop shrinking.
#
# After shrinking, window is [6 .. 10], have = 2, res still [0,5] (length 6).
#
# r=11, add 'N' → have = 2.
#
# r=12, add 'C'
#
# C becomes 1 → have = 3 == need → window [l=6 .. r=12] is VALID
#
# Current length = 7 (bigger than current best 6), try to shrink:
#
# shrink s[6]='O' → not required → l=7, have=3
#
# shrink s[7]='D' → not required → l=8, have=3
#
# shrink s[8]='E' → not required → l=9, have=3
#
# Now window is [9 .. 12], length = 4. This is smaller than reslen=6 → update res = [9,12], reslen = 4.
#
# continue shrinking: remove s[9]='B' → B becomes 0 (< required) → have = 2, l=10 → stop.
#
# End of loop. Final res = [9,12] → substring s[9:13] = "BANC".


