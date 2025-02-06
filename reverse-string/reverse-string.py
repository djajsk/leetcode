class Solution:
    
    def recu(self,s,ind1,ind2):
        
        if ind2 <= ind1:
            return 
        
        var1 = s[ind1]
        var2 = s[ind2]
        
        s[ind2] = var1
        s[ind1] = var2
        
        self.recu(s,ind1+1,ind2-1)
        
        
        
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)-1
        self.recu(s,0,n)
        
        
        