# HLAWR was here!

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = [matches[i][1] for i in range(len(matches))]
        ans1 = [i for i in loser if loser.count(i) == 1]
        winner = [matches[i][0] for i in range(len(matches))]
        ans0 = [i for i in winner if loser.count(i) == 0]
        return [sorted(set(ans0)),sorted(set(ans1))]
