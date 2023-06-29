class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if len(s) != len(t):
        #for i in s:
         #   if s.count(i) != t.count(i):
          #      return False
        
        if len(s) >= len(t):
            for i in s:
                if s.count(i) != t.count(i):
                    return False
                    
        if len(t) > len(s):
            for i in t:
                if s.count(i) != t.count(i):
                    return False
        return True
            
        