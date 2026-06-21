class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


nums = [3, 2, 4]
sol = Solution()
print(sol.twoSum(nums, 6))
