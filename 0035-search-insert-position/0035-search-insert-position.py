class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                
        if nums[-1] < target:
            return len(nums)
        
        if nums[0] >= target:
            return 0
                
        else:
            for i in range(len(nums)):
                if nums[i] > target and nums[i-1] < target:
                    return i
            
        