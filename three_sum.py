class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            #if the next value is duplicate we have to continue to next loop
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l<r:
                threesum = a + nums[l] + nums[r]

                if threesum >0:
                    r=r-1
                elif threesum<0:
                    l=l+1
                else:
                    res.append([a,nums[l], nums[r]])
                    l=l+1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res