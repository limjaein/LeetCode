class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1
        s = s.lstrip()
        num = 0
        isNegative = False
        
        # 2
        if len(s) > 0:
            if s[0] == '-':
                isNegative = True
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
        
        # 3
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        
        # 4
        i = 0
        while i < len(s): 
            if s[i] == '0':
                s = s[i:]
                i += 1
            else:
                break
        
        if len(s) == 0:
            s = "0"
        
        # 5
        if isNegative:
            if int(s) > 2**31:
                s = str(-1*2**31)
            else:
                s = '-' + s
        else:
            if int(s) >= 2**31:
                s = str(2**31-1)
        
        return int(s)
            