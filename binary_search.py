class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# Main program
nums = [-1, 0, 3, 5, 9, 12]
target = 9

solution = Solution()
res = solution.search(nums, target)
if res == -1:
    print(res)
else:
    print(res)
