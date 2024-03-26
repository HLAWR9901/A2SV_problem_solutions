class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        state = True
        while state:
            state = False
            i = 1
            while i < n:
                if nums[i] != 0 and nums[i] == nums[i - 1]:
                    nums[i - 1] *= 2
                    nums[i] = 0
                    state = True
                i += 1
        nums = [x for x in nums if x != 0] 
        nums += [0] * (n - len(nums))
        return nums
