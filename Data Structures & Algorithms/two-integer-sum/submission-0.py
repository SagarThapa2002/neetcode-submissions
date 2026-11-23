class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={} # value - index
        for i, num in enumerate(nums): # gives each number position and value
            partner = target - num
            if partner in seen:
                return [seen[partner], i]
            seen[num]=i