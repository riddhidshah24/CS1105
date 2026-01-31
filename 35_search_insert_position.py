class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
#linear search 
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)
