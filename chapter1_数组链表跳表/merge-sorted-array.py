
def merge1(nums1, m, nums2, n):
    i = 0
    while i != n:
        nums1[m + i] = nums2[i]

    nums1.sort()


def merge(nums1, m, nums2, n):
    # len(nums1) > len(nums2)
    # 有序整数数组 nums1 和 nums2
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1] #
            m -= 1
        else:
            nums1[m + n -1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]