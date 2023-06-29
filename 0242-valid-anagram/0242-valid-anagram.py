class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #if len(s) != len(t):
        #for i in s:
         #   if s.count(i) != t.count(i):
          #      return False
        
        '''if len(s) >= len(t):
            for i in s:
                if s.count(i) != t.count(i):
                    return False
                    
        if len(t) > len(s):
            for i in t:
                if s.count(i) != t.count(i):
                    return False
        return True'''
        
        s = [i for i in s]
        t = [i for i in t]
        a = s.sort()
        b = t.sort()
        if s == t:
            return True
        return False
        