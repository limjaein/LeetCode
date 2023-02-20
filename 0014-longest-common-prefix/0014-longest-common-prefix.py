class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        
        # input arr를 길이별로 정렬
        strs.sort(key=len)
        
        # 가장 짧은 문자열을 기준으로 전체 검색
        short_str = strs[0]
        
        l = len(short_str)
        
        while l > 0:
            cnt = 0
            
            for j in range(1, len(strs)):
                if short_str[0:l] == strs[j][0:l]:
                    cnt += 1

            if cnt == len(strs) - 1:
                return short_str[0:l]
            
            l -= 1
        
        return result
        