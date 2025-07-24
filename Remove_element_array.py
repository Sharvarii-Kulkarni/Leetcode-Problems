def remove(nums,val):
    k=0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k=k+1
    return k

nums = [8,9,8,9,7,8]
print(remove(nums,8))