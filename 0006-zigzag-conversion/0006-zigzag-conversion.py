class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        numCols = self.getColNum(s, numRows) 
        
        return self.getZigzagPattern(s, numRows, numCols)
        
    
    def getColNum(self, s, r):
        c = 0
        l = len(s)
        
        while l > 0:
            l -= r
            c += 1
            
            if l > 0:
                n = min(l, r - 2)
                l -= n
                c += n
        return c
    
    
    def getZigzagPattern(self, s, r, c):
        pattern = [['' for _ in range(c)] for _ in range(r)]
        
        y = 0
        x = 0
        l = 1
        isEnd = False
        ret = ""

        pattern[y][x] = s[0]
        
        while not isEnd:
            for _ in range(r - 1):
                if l == len(s):
                    isEnd = True
                    break
                y += 1 # 아래로 이동
                pattern[y][x] = s[l]
                l += 1
            
            for _ in range(r - 1):
                if l == len(s):
                    isEnd = True
                    break
                x += 1
                y -= 1 # 대각선 위로 이동
                pattern[y][x] = s[l]
                l += 1
        
        for i in range(r):
            ret += ''.join(pattern[i])
        
        return ret
        
        
        