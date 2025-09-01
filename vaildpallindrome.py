class Solution:
    def ispallindrome(self,str)->bool:
        l,r=0,len(str)-1
        while l<r:
            while l<r and not self.aplhanum(str[l]):
                l+=1
            while r>l and not self.aplhanum(str[r]):
                r-=1
            if str[l].lower!=str[r].lower:
                return False
            l,r=l+1,r-1
        return True

    def aplhanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
sol=Solution()
print(sol.ispallindrome("isi malayalam isi"))