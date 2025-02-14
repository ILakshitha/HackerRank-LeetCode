class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):  
            seen = set()  # Track visited characters
            temp = 0  
            
            for j in range(i, len(s)):  
                if s[j] in seen:  # Stop if a duplicate is found
                    break
                
                seen.add(s[j])  
                temp += 1  # Increase the count for the substring
                
                count = max(count, temp)  # Update max length
        
        return count