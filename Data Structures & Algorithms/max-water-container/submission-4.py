class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxx=0
        for i in range(len(heights)):
            water=min(heights[left],heights[right])*(right-left)
            maxx=max(water,maxx)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxx
