class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            a=nums.copy()
            del a[i]
            p=1
            for j in a:
                p *= j
            res.append(p)
        return res