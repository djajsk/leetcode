class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        a = num**0.5
        if a.is_integer():
            return True
        else:
            return False
        