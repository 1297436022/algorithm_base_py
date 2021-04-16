

def move_zeroes(nums):  # 双指针 快排思想
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    # 两个指针i和j
    j = 0
    for i in range(len(nums)):
        # 当前元素!=0，就把其交换到左边，等于0的交换到右边
        if nums[i] & i > j:  # i > j 避免 i=j 的交换
            nums[j], nums[i] = nums[i], nums[j]  # 交换nums[i] 和 nums[j]
            j += 1

    print(nums)


move_zeroes([2, 1, 0, 3, 12])


def move_zeroes1(nums):  # 先统计0的个数
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    # 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    # 非0元素统计完了，剩下的都是0了
    # 所以第二次遍历把末尾的元素都赋为0即可
    for i in range(j, len(nums)):
        nums[i] = 0

