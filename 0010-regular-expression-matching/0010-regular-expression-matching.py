import re


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        c_p = re.compile(p)
        m = c_p.match(s)
        
        if m is not None and s == m.group():
            return True
        else:
            return False