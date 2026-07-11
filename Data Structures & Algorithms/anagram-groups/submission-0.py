class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = dict()

        for word in strs:
            lst = [0]*26
            for char in word:
                val = ord(char)-ord("a")
                lst[val]+=1
            
            tup = tuple(lst)
            if store.get(tup, False):
                store[tup].append(word)
            else:
                store[tup] = [word]
            
        
        fans = []
        for key, val in store.items():
            fans.append(val)
        
        return fans