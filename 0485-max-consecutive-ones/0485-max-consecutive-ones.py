class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        lis = []
        
        for i in nums:
            if i == 1:
                count += 1
            else:
                lis.append(count)
                count = 0
        lis.append(count)
        return max(lis)