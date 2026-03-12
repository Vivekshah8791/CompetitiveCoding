class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        total=0
        count=0
        for i in range(len(nums)):
            if nums[i]<=right:
                count+=1
            else:
                count=0
            total+=count
        total2=0
        count2=0
        for i in range(len(nums)):
            if nums[i]<=left-1:
                count2+=1
            else:
                count2=0
            total2+=count2
        return total-total2

        
            