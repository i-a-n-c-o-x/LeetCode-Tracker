class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        boolean = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                boolean.append(True)
            else:
                boolean.append(False)
        return boolean

        