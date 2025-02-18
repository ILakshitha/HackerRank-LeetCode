class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []  # Using a set to avoid duplicates

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:  
                    result.append(words[i])  
                    break  

        return result  # Convert set to list before returning
