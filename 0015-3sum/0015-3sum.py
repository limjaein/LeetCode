class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        num_length = len(nums)
        nums.sort()
        
        for i in range(num_length):
            if nums[i] <= 0:
                if i != 0 and nums[i-1] == nums[i]:
                    continue
                l = i + 1
                r = num_length - 1
                
                while l < r:
                    if i != l-1 and nums[l-1] == nums[l]:
                        l += 1
                    else:
                        if nums[i] + nums[l] + nums[r] == 0:
                            result.add((nums[i], nums[l], nums[r]))
                            l += 1
                        elif nums[i] + nums[l] + nums[r] < 0:
                            l += 1
                        else:
                            r -= 1

        return result