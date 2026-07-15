class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        a=[]
        for i in sorted_freq[:k]:
            a.append(i[0])
        return a

            