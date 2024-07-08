class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        winner = [i for i in range(1, n+1)]
        index = 1
        while len(winner) > 1:
            val = winner.pop(0)

            if index % k != 0:
                winner.append(val)

            index += 1
        return winner[0]



