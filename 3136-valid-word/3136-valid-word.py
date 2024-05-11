class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) <3:
            return False
        
        vowel = ['a','e','i','o','u']
        vowels = []
        cons = []
        nums = []
        extra = []
        
        for i in word:
            if i.lower() in vowel:
                vowels.append(i)
            elif i.isalpha() and i.lower() not in vowels:
                cons.append(i)
                
            elif i.isnumeric():
                nums.append(i)
            else:
                extra.append(i)
        
        if len(extra) > 0:
            return False
        if len(vowels) > 0 and len(cons) >0:
            return True
        
        
        