
def remove_duplicates(nums):

    n = len(nums)
    if n is 0:
        return 0

    fast, slow = 1, 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow

print(remove_duplicates([1,1,3]))