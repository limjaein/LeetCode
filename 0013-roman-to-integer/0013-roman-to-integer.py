class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        # MCMXCIV"
        prev = ''
        cur = ''
        sum = 0
        i = 0
        
        while True:
            if i >= len(s) - 1:
                while i < len(s):
                    sum += roman_dict[s[i]]
                    i += 1
                break
            prev = roman_dict[s[i]]
            cur = roman_dict[s[i+1]]
            
            l_prev = len(str(prev))
            l_cur = len(str(cur))
            
            if l_prev < l_cur or (l_prev == l_cur and prev < cur):
                sum += (cur - prev)
                i += 1
            else:
                sum += prev
            
            i += 1
                
        return sum