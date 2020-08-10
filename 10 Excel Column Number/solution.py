class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0 
        for letter in s:
            res*=26
            res += (ord(letter) - ord('A') + 1)
            
        return res