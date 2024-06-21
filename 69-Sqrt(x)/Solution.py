#Time: O(Log(n))
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 # Start at start
        r = x

        while l <= r:
            m = (l + r) // 2 # Floor division
            mid_squared = m * m

            if mid_squared < x:
                l = m + 1
            elif mid_squared > x:
                r = m - 1 # Shifts the stream of ints
            else: # is equal to x so return index
                return m

        return r
