class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        # Base cases
        if n <= 1:
            return 1
        
        # Create a list to store the results of subproblems
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1

        # Fill the dp list using dynamic programming
        for i in range(2, n + 1):
            # If there's a move that leaves the opponent in a losing position, take it
            if dp[i - 1] == 0:
                dp[i] = 1
            elif i - x >= 0 and dp[i - x] == 0:
                dp[i] = 1
            elif i - y >= 0 and dp[i - y] == 0:
                dp[i] = 1
            else:
                dp[i] = 0

        # Return the result for n
        return dp[n]
