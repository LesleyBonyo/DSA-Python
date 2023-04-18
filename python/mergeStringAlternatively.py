class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        if len(word1) <= len(word2):
            for i in range(len(word1)):
                merged += word1[i] + word2[i]
            merged += word2[len(word1):]

        if len(word2) < len(word1):
            for i in range(len(word2)):
                merged += word1[i] + word2[i]
            merged += word1[len(word2):]

        return merged
