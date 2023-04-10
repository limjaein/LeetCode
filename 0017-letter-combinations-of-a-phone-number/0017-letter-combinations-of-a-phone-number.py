result = set()
button = [[], [], ['a','b','c'], ['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'], ['w','x','y','z']]

class Solution(object):
    
    def setLetters(self, i, nums, s, l, result):
        if len(s) == l:
            result.add(s)
            return
            
        num = nums[i]
        
        for b in button[num]:
            self.setLetters(i+1, nums, s + str(b), l, result)
        
            
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = set()
        
        nums = map(int, list(digits))
        
        if len(digits) > 0:
            self.setLetters(0, nums, "", len(digits), result)
        
        return result