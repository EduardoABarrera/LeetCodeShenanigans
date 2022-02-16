import math, time

class Solution:
    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (target == nums[i] + nums[j]): 
                    return [i, j]
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                print(complement)
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
