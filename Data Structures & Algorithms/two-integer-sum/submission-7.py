class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {num: ind for ind, num in enumerate(nums)}

        for index, num in enumerate(nums):
            if (target - num) in hashMap and index != hashMap[target-num]:
                return [index, hashMap[target - num]]