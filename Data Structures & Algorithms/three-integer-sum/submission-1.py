class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left=1
        k=0
        nums=sorted(nums)
        res=[]
        right=len(nums)-1
        for k in range(len(nums)):
            if k>0 and nums[k]== nums[k-1]:
                continue
            left=k+1
            right=len(nums)-1
            while left<right:
                ad=nums[k]+nums[left]+nums[right]
                if ad==0:
                    res.append([nums[left],nums[right],nums[k]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif ad>0:
                    right-=1
                elif ad<0:
                    left+=1
        return res