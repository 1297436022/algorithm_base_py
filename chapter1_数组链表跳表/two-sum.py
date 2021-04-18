
def two_sum(nums, target):
    hashtable = dict()
    for i in range(len(nums)):
        if nums[i] in hashtable:
            return [hashtable[nums[i]], i]  # 返回索引
        else:
            hashtable[target - nums[i]] = i  # 索引 内容


print(two_sum([2, 7, 11, 15], 9))
