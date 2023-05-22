class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 만약 홀수면 중간 idx 위치 값을 리턴
        # 짝수면 중간 두 idx 위치 값의 평균을 리턴
        
        l_i = 0
        r_i = 0
        l = len(nums1) + len(nums2)
        isOdd = l % 2 == 1
        idx = l / 2
        prev = 0
        target = -1
        
        while True:
            # 인덱스를 먼저 이동하기 때문에, 인덱스 예외 처리
            if r_i >= len(nums2) or (l_i < len(nums1) and nums1[l_i] < nums2[r_i]):
                target = nums1[l_i]
                l_i += 1
            else:
                target = nums2[r_i]
                r_i += 1
                
            if not isOdd:                
                # 짝수일 경우 직전 숫자 저장
                if l_i + r_i == idx:
                    prev += target
                
            if idx == l_i + r_i - 1:
                if isOdd:
                    return target
                else:
                    return (prev + target)/2.0
                    
                    