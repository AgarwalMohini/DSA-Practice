class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=''
        count=0
        for char in s:
            if char=='(':
                if count>0:
                    res+='('
                count+=1
            else:
                count-=1
                if count>0:
                    res+=')'
        return res