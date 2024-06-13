class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = 0
        seats.sort()
        students.sort()

        for index in range(len(seats)):
            moves += abs(seats[index] - students[index])
            

        return moves
