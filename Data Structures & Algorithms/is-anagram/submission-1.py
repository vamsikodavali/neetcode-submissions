class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store_s = dict()
        i = 0

        if len(s)!=len(t):
            return False
            
        while i<len(s):
            
            ct = store_s.get(s[i], 0)
            
            if ct == 0:
                store_s[s[i]] = 1
            else:
                store_s[s[i]] += 1

            i+=1

        i = 0
        while i<len(t):

            ct =  store_s.get(t[i], 0)

            if ct==0:
                return False
            else:
                store_s[t[i]] -= 1
            
            i+= 1
            
        return True
        