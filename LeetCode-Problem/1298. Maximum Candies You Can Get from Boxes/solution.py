class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        queue = deque(initialBoxes)
        visited = [False] * n
        waiting = set()
        haveKey = set()
        total = 0

        while queue:
            box = queue.popleft()
            if visited[box]:
                continue
            if status[box] == 1 or box in haveKey:
                visited[box] = True
                total += candies[box]
                for key in keys[box]:
                    haveKey.add(key)
                    if key in waiting:
                        queue.append(key)
                        waiting.remove(key)
                for contained in containedBoxes[box]:
                    if not visited[contained]:
                        if status[contained] == 1 or contained in haveKey:
                            queue.append(contained)
                        else:
                            waiting.add(contained)
            else:
                waiting.add(box)
        return total
            
