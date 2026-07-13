#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = dict()
        n_2 = len(nums)//2
        for ind, val in enumerate(nums):
            if store.get(val, -1) == -1:
                store[val]=1
            else:
                store[val] += 1
                
            if store[val]>n_2:
                return val
        
        return  -1

        
# @lc code=end

