class solution:
    def validparanthesis(self,s:str)->bool:
        stack=[]
        closetoopen={")":"(","}":"{","]":"["}
        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
sol=solution()
print(sol.validparanthesis("{[()]}"))




