class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        
        for num in nums:
            if num in hashtable.keys():
                hashtable[num] += 1  
            else:
                hashtable[num] = 1 
            
            if hashtable[num] > (len(nums) / 2):
                return num
