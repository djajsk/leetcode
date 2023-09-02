class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n = len(nums)
        lis = []
        k = k % n
            
        for i in range(n-k,n):
            lis.append(nums[i])
        for j in range(0,n-k):
            lis.append(nums[j])
            
        
            
        for i in range(n):
            nums[i] = lis[i]
        
        