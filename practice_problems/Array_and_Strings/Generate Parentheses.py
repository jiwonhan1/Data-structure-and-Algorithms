class Solution(object):
    def generateParenthesis(self,n):
        ans = []
        def backtrack(S, left, right):
            if len(S) == n*2:
                ans.append("".join)
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack([],0,0)
        return ans