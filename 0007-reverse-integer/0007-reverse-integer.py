class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = int(str(x).rstrip("0")[::-1])
            if x >= -2**31 and x <= 2**31-1:
                return x
        elif x < 0:
            x = int(str(x).rstrip("0")[1:][::-1])
            if x >= -2**31 and x <= 2**31-1:
                return x * -1
        
        return 0