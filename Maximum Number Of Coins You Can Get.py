class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # why not this
        # piles.sort(reverse=True)
        # return sum(piles[i] for i in range(1, len(piles), 3))
        piles.sort()
        n = len(piles)
        i = 0
        j = n - 1
        res = 0
        count = n // 3
        while i < j and count != 0:
            if i < j - 1:
                res += piles[j - 1]
                count -= 1
            i += 1
            j -= 2
        return res
