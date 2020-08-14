class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        seen = set()
        for letter in s:
            if letter not in seen:
                seen.add(letter)
            else:
                seen.remove(letter)
         
        if len(seen) >= 1:
            return len(s) - len(seen) + 1
        else:
            return len(s) - len(seen)
            