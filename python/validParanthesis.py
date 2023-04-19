class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #myDict = {}
        for i in range(0, len(s), 2):
            if i < len(s)-1:
                if s[i] == '(' and s[i+1] == ')':
                    return True
                if s[i] == '[' and s[i+1] == ']':
                    return True
                if s[i] == '{' and s[i+1] == '}':
                    return True

        return False
