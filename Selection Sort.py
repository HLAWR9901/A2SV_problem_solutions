# HLAWR was here!

class Solution: 
    def select(self, arr, i):
        # code here 
        selectionSort(arr,n)
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            sub_arr = arr[i:n]
            min_val = min(sub_arr)
            min_index = arr.index(min_val)
            arr[i], arr[min_index] = arr[min_index], arr[i]
 

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
