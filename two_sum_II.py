class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0, len(numbers)-1

        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum >target:
                r = r-1
            elif curSum < target:
                l = l+1
            else:
                return [l+1, r+1]
        return []
