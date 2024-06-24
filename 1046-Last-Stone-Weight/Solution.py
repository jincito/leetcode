class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: # Continue while number of stones is greater than 1, or if we have 0 stones we can stop
            first = heapq.heappop(stones)  # Largest stone in heap
            second = heapq.heappop(stones) # Second largest
            if second > first: # Opposite b/c -7 > -8
                heapq.heappush(stones, first - second)

        stones.append(0) # edge case: stones == empty
        return abs(stones[0])

# Time: O(n Log(n))
# Space: O(n)
