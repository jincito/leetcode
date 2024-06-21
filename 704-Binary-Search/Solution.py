class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 # start of array
        r = len(nums) - 1 # set right pointer to length of array - 1 index
        while l <= r: # condition exits when left and right pointer meet
            m = (l + r) // 2 # set middle index
            n = nums[m] # set middle element in the array
            if n < target:
                l = m + 1 # update the left pointer shifting the range
            elif n > target:
                r = m - 1 # update the right pointer shift range
            else: # n == target, they are equal so return index
                return m
        return -1  # target not found
