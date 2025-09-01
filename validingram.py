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


