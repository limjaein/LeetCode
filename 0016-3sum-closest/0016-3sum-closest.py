class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(l):
            j = i+1
            k = l-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    result = s
                    break
                elif s < target:
                    j += 1
                else:
                    k -= 1
                
                if abs(target - s) < abs(target - result):
                    result = s
            
            if result == target:
                break
        
        return result