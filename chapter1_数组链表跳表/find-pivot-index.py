
def pivot_index(nums):
    # S ： 全部元素之和
    # A :  x左边元素之和
    # B = S - A - X  又  A = B
    # 所以 A = S - A - X  -->  2 * A + X = S

    S, A = 0, 0
    for i in range(len(nums)):
        S += nums[i]

    for i in range(len(nums)):
        x = nums[i]
        if 2 * A + x is S:
            return i
        A += x

    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))