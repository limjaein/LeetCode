class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        symbol = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        result = ""
        
        while num > 0:
            first = str(num)[0]
            l = len(str(num)) - 1
            
            if first == "4":
                result += symbol.get(10**l) + symbol.get(5*10**l)
                num -= 4 * 10**l
            elif first == "9":
                result += symbol.get(10**l) + symbol.get(10**(l+1))
                num -= 9 * 10**l
            else:
                if num >= 5 * 10**l:
                    result += symbol.get(5*10**l)
                    num -= 5 * 10**l
                
                for i in range(num/10**l):
                    result += symbol.get(10**l)
                    num -= 10**l
            
        return result
                    
                        