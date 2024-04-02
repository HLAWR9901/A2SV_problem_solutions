class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # using counting sort
        max_val = max(nums) + 1 
        arr = [0] * max_val
        for num in nums:  
            arr[num] += 1
        
        new_arr = []
        for i in range(len(arr)):  
            while arr[i] > 0: 
                new_arr.append(i)
                arr[i] -= 1
        
        nums[:] = new_arr

        
