class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = dict()
        for i, val in enumerate(nums):
            ct = store.get(val, 0)
            if ct==0:
                store[val] = 1
            else:
                return True
        
        return False
        