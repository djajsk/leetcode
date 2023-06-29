class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        a = title.lower()
        a= a.split()
        c= []
        
        for i in a:
            if len(i) > 2:
                b = i.capitalize()
                c.append(b)
            else:
                c.append(i)
            
        return " ".join(c)
            
        
        