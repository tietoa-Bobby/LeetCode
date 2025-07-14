class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        if num == num[::-1]:
            return True
        else:
            return False
        