
def three_sum(nums):
    n = len(nums)
    res = []
    if not nums or n < 3:
        return []
    nums.sort()
    res = []
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left + 1] == nums[left]:
                    left = left + 1
                while left < right and nums[right - 1] == nums[right]:
                    right = right - 1
                left = left + 1
                right = right - 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right = right - 1
            else:
                left = left + 1
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
