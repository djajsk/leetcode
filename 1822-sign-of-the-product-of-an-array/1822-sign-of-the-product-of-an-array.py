class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        
        sign = 0
        for i in range(0,len(nums)):
            if nums[i] < 0:
                sign += 1
            if nums[i] == 0:
                return 0
        
        if sign%2 == 0:
            return 1
        else:
            return -1
            
            
        
        