class Solution:
    def minOperations(self, n: int) -> int:
        @cache
        def f(x):
            if x <= 1: return x
            return 1+min(f(x-1), f(x+1)) if x%2==1 else f(x//2)
        return f(n)