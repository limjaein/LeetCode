import itertools

class Solution(object):
    def addParenthesis(self, s, l_cnt, r_cnt, n, result):
        if l_cnt == n and r_cnt == n:
            result.add(s)
            return
        
        if l_cnt < n:
            self.addParenthesis(s + "(", l_cnt + 1, r_cnt, n, result)
            
        if r_cnt < n and l_cnt > 0 and l_cnt > r_cnt:
            self.addParenthesis(s + ")", l_cnt, r_cnt + 1, n, result)
            
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        result = set()
        
        l_cnt = 1
        r_cnt = 0
        self.addParenthesis("(", l_cnt, r_cnt, n, result)
        
        return list(result)
        
    