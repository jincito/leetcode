# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Time: O(Log n)
# Space: O(n)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right: # Use <= to take care of 1 number input
            mid = (left + right) // 2
            if isBadVersion(mid):
                firstBad = mid # Store mid in firstBad
                right = mid - 1
            else:
                left = mid + 1
        return firstBad

