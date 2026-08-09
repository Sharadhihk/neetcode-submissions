class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        for i in range(len(nums)):
            if nums[i] in groups:
                groups[nums[i]]+=1
            else:
                groups[nums[i]]=1
        res=sorted(groups,key=groups.get,reverse=True)
        return res[:k]
        