class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n;
        else:
            return 2*n;
'''
 LCM * GCF = n*2 
 GCF = 1 if n is odd and GCF = 2 if n is even 
 '''
