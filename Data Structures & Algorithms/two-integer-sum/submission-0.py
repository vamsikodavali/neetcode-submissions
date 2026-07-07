class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = dict()

        for i, val in enumerate(nums):
    
            req = target-val

            curr_ind = store.get(val, -1)
            req_ind = store.get(req, -1)

            if req_ind != -1:
                return [req_ind, i]

            if curr_ind==-1:
                store[val] = i
            else:
                continue
        
        return []

        