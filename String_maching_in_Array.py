class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []  # Using a set to avoid duplicates

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:  # Ensuring i and j are different
                    result.append(words[i])  # Add to set instead of list
                    break  # No need to check further if already found

        return result  # Convert set to list before returning
