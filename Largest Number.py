class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=lambda x: x * 10, reverse=True)
        return ''.join(nums_str)
