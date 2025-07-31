class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canFinish(k):
            """Check if Koko can finish all bananas with eating speed k within h hours"""
            hours_needed = 0
            for pile in piles:
                # Calculate hours needed for this pile (ceiling division)
                hours_needed += (pile + k - 1) // k  # equivalent to math.ceil(pile / k)
            return hours_needed <= h
        
        # Binary search on eating speed
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                # Can finish with speed mid, try smaller speed
                right = mid
            else:
                # Cannot finish with speed mid, need faster speed
                left = mid + 1
        
        return left
        