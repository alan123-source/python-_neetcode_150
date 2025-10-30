class Solution:
    def isAnagram(self,S:str,T:str)-> bool:
        if len(S)!=len(T):
            return False
        countS,countT={},{}
        for i in range(len(S)):
            countS[S[i]]=1+countS.get(S[i],0)
            countT[T[i]]=1+countT.get(T[i],0)
        for c in countS:
            if countS[c]!=countT[c]:
                return False
        return True
sol=Solution()
print(sol.isAnagram("anagram","aangram"))

#ithengana work chyunan vechal adyam length check chym if they are not equal
# false return chym equal anenkil nml len(s) etrayano ath vare nokm  sil ipm
# olla elementit count  hash mapiloode nml count edukunoo enit count check chyunoo
# count chyth vech sambhavham ipm hash tablilond so ath rand hash tabilile count ayit nokm if they are not
# then it is not anangram

# #optimized solution using one hash table
# def isAnagram(self, S: str, T: str) -> bool:
#     if len(S) != len(T):
#         return False
#
#     count = {}
#     for c in S:
#         count[c] = 1 + count.get(c, 0)   # increase count for each char in S
#
#     for c in T:
#         if c not in count:
#             return False
#         count[c] -= 1                   # decrease for each char in T
#         if count[c] < 0:                # more occurrences in T than in S
#             return False
#
#     return True
#here we increment 1 for each charecter in s and decrement 1
#for each char in t  finaly if count is 0 it is valid else not valid

