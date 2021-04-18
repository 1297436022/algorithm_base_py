import copy

def reverse(nums, start, end):
    while start < end:
        nums[end], nums[start] = nums[start], nums[end]
        start += 1
        end -= 1

def rotate1(nums, k):

    # nums = "----->-->" k = 3
    # result = "-->----->"
    # reverse "----->-->" we can get "<--<-----"
    # reverse "<--" we can get "--><-----"
    # reverse "<-----" we can get "-->----->"
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums


def rotate(nums, k):
    n = len(nums)
    new_arr = [None] * n #

    for i in range(0, len(nums)):
        new_arr[(i + k) % n] = nums[i] #

    nums[:] = new_arr[:]
    # nums = copy.copy(new_arr)
    return nums


print(rotate1([1, 2, 3, 4, 5, 6], 2))