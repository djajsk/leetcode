class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        right = sum(nums)
        
        for i in range (0,len(nums)):
            right = right - nums[i]
            if right == left:
                return i
            
            left += nums[i]
        return -1
            
            
        