class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup = set()
        l = 0
        r = 0 # l = save, r = search
        
        for num in nums:
            if num not in dup:
                dup.add(num)
                nums[l] = num
                l += 1
                r += 1
            else:
                r += 1
        
        return l