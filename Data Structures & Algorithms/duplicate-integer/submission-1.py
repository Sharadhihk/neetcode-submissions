class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fseen = set()
        for x in nums:
            if x in fseen:
        # We found a match!
                return True
            fseen.add(x)
        return False  