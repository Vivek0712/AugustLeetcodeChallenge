class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        if ord(word[0]) >= 65 and ord(word[0]) <=90:
            if ord(word[1]) >= 65 and ord(word[1]) <=90:
                for w in range(2,len(word)):
                    if not(ord(word[w]) >= 65 and ord(word[w]) <=90):
                        return False
            else:
                for w in range(2,len(word)):
                    if not(ord(word[w]) >= 97 and ord(word[w]) <=122):
                        return False
                
        else:
            for w in range(1,len(word)):
                    if not(ord(word[w]) >= 97 and ord(word[w]) <=122):
                        return False
        return True
            