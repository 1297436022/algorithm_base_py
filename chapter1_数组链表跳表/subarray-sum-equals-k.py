def subarraySum(nums, k):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1

    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums - k, 0)
        d[sums] = d.get(sums, 0) + 1

    return count
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
print(subarraySum([1,1,1], 2))