class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        length = 1
        answer = s[0]
        
        l_idx = 0
        r_idx = 0
        
        while r_idx < len(s) - 1:
            r_idx += 1
            
            while l_idx != r_idx and s[r_idx] in s[l_idx:r_idx]:
                l_idx += 1
            
            answer = s[l_idx:r_idx + 1]
            length = max(length, len(answer))
        
        return length
        