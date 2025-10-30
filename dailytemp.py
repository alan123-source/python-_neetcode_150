class solution:
    def dailytemp(self,temperature:list[int])->list[int]:
        res=[0]*len(temperature)
        stack=[]
        for i,t in enumerate(temperature):
            while stack and t>stack[-1][0]:
                stacktemp,stackind=stack.pop()
                res[stackind]=(i-stackind)
            stack.append([t,i])
        return res