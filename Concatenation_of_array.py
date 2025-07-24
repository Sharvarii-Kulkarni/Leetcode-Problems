nums = [1,2,3]
n=len(nums)

ans = []

for i in range(0,n-1):
    for num in nums:
        ans.append(num)

print(ans)