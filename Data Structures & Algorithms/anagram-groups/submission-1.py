class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        aaa=[]
        for i in range(len(strs)):
            if strs[i] in aaa:
                continue
            abc=[]
            abc.append(strs[i])
            aaa.append(strs[i])
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    abc.append(strs[j])
                    aaa.append(strs[j])
            res.append(abc)
        return res

