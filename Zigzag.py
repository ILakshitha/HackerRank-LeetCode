class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  

        rows = [''] * numRows  # Initialize rows
        cur = 0                # Current row index
        step = 1               # Direction (down = +1, up = -1)

        for ch in s:
            rows[cur] += ch
            if cur == 0:
                step = 1       # Go down
            elif cur == numRows - 1:
                step = -1      # Go up
            cur += step

        return ''.join(rows)