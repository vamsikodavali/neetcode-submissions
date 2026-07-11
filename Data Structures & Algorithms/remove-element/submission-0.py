class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ct = nums.count(val)
        k =  len(nums) - ct
        ind = -1
        i=0
        while i<len(nums):

            if nums[i]!=val:
                if ind==-1:
                    pass
                else:
                    nums[ind] = nums[i]
                    ind += 1
            else:
                if ind==-1:
                    ind = i

                

            i+=1

        # ct = nums.count(val)
        return k
        