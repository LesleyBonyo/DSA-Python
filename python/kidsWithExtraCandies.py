class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # get the max. iterate through the array adding extracandies
        # if value is greater or equal to max, add true to array else false
        result = []
        maxValue = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxValue:
                result.append(True)
            else:
                result.append(False)
        return result
