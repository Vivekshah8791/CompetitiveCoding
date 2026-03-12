class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums) - x
        left = 0
        sumi = 0
        length = -1
        if total < 0:
            return -1
        for j in range(len(nums)):
            sumi += nums[j]
            while sumi > total and left <= j:
                sumi -= nums[left]
                left += 1
            if sumi == total:
                length = max(length, j - left + 1)
        if length == -1:
            return -1
        else:
            return len(nums) - length