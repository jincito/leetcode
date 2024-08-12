class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two pointers
        # find the longest substring by incrementing a max variable
        # it increments after finding a unique character in substring
        n = len(s)
        left = 0
        maxLength = 0
        charSet = {} # Key: Character, Value: Index

        for right in range(n):
            # Unique character
            if s[right] not in charSet or charSet[s[right]] < left:
                charSet[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            # Repeated Character
            else:
                left = charSet[s[right]] + 1
                charSet[s[right]] = right

        return maxLength

