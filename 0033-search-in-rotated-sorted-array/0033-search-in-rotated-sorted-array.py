class Solution(object):
    def binary_search(self, nums, s, e, target):
        if e - s < 0:
            return -1
        
        mid = (s + e) / 2
        
        # 순방향
        if nums[mid] == target:
            return mid
        
        if nums[s] <= nums[mid]:
            if nums[s] <= target < nums[mid]:
                return self.binary_search(nums, 0, mid - 1, target)
            else:
                return self.binary_search(nums, mid + 1, e, target)
        else:
            print(nums[mid],target,nums[s])
            if nums[mid] <= target < nums[s]:
                return self.binary_search(nums, mid + 1, e, target)
            else:
                return self.binary_search(nums, 0, mid - 1, target)
                
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        return self.binary_search(nums, 0, len(nums) - 1, target)