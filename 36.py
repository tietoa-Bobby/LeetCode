import collections

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Use defaultdicts of sets to track seen numbers for each row, column, and 3x3 box.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # Key will be (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Skip empty cells
                if num == '.':
                    continue

                box_key = (r // 3, c // 3)

                # Check for duplicates in the current row, column, and 3x3 box
                if num in rows[r] or num in cols[c] or num in boxes[box_key]:
                    return False

                # Add the number to the corresponding sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_key].add(num)

        return True