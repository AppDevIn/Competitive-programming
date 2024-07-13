class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        path = {}
        for index in range(len(positions)):
            path[positions[index]] = (healths[index], directions[index], index)

        stack = []
        for pos in sorted(positions):
            health, direction, index = path[pos]
            if direction == "R":
                stack.append(pos)
            else:
                while stack:
                    rigthPos = stack.pop(-1)
                    rightHealth, rightDirection, rightIndex = path[rigthPos]
                    if rightHealth > health:
                        path[rigthPos] = (rightHealth - 1, rightDirection, rightIndex)
                        stack.append(rigthPos)
                        healths[index] = 0
                        healths[rightIndex] = rightHealth - 1
                        break
                    elif rightHealth < health:
                        health -= 1
                        healths[rightIndex] = 0
                        healths[index] = health
                    else:
                        healths[rightIndex] = 0
                        healths[index] = 0
                        break

        return [health for health in healths if health != 0]

