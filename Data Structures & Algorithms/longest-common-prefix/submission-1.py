class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""

        min_len = float("+inf")
        for val in strs:
            min_len = min(min_len, len(val))
        
        i = 0
        ans_found = False

        while i<min_len:
            
            ch = None
            for ind, val in enumerate(strs):
                
                if ind>0:
                    if val[i] != ch:
                        ans_found = True
                        break
                else:
                    ch = val[i]
            
            if ans_found:
                return ans
            
            else:
                ans = val[:i+1]




            i+=1


        return ans
        