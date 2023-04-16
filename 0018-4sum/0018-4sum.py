class Solution(object):
    def getQuadruplets(self, nums, target):
        l = len(nums)
        tmp = set()
        
        for i in range(l-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, l-2):
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, l-1):
                    if k-1 != j and nums[k] == nums[k-1]:
                        continue
                    for h in range(l-1, k, -1):
                        if h-1 != k and nums[h] == nums[h-1]:
                            continue
                            
                        s = nums[i] + nums[j] + nums[k] + nums[h]
                        
                        if s == target:
                            tmp.add((nums[i], nums[j], nums[k], nums[h]))
                        elif s < target:
                            break
                        
                        if h == k+1 and k == j+1 and j == i+1 and s > target:
                            return tmp
        return tmp
        
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        tmp = set()
        result = []
        
        tmp = self.getQuadruplets(nums, target)

        for p in tmp:
            result.append(list(p))
        
        return result