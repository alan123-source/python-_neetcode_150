class solution:
    def evalrpn(self,tokens:list[str])->int:
        stack=[]
        for c in tokens:
            if c == "+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
# #ivde enthukond / charecter load chyumbm matram
# int upayodichoo en oru chodyam varum
# thats because  nml oru charectara varumbm athine int
# akiyan store chyun so for  / float value varm so ath patila
# baky operations chuyumbm ath already int value an return chyun
# stack[o] means returns the value if only one element left and
# stack [-1] returns the top value stack[0] varubm aa stackile
# index 0 olla value return akum
# but stack [-1 ] top element return chym ivde oru elemete last
# remain chyunolloo thats why we get stack[o] kodukumbm  aa elementb
# kitun