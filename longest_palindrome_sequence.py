import math

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        lgsub = s[0]  # Initialize with the first character (smallest possible palindrome)
        
        for i in range(len(s)):
            # Check for odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(lgsub):
                    lgsub = s[left:right+1]
                left -= 1
                right += 1
            
            # Check for even-length palindromes
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(lgsub):
                    lgsub = s[left:right+1]
                left -= 1
                right += 1
        
        return lgsub
    