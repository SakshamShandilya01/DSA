class Solution(object):
    def maximumCount(self, nums):
        positive = 0
        negative = 0

        for i in nums:
            if (i > 0):
                positive += 1
            elif (i < 0):
                negative += 1

            else:
                return 0

        if (positive > negative):
           return positive

        else:
              return negative