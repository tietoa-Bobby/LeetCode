class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False