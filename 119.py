class Solution(object):
    def getRow(self, rowIndex):
        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - k + 1) // k 
            res.append(next_val)
            prev = next_val
        return res
        