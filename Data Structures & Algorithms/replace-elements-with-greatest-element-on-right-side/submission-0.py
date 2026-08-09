class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_right=-1
            for j in range(i+1,len(arr)):
                if arr[j] > max_right:
                    max_right=arr[j]
            arr[i]=max_right
        return arr