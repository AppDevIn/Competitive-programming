class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = rooms[0]
        visited = [0]
        while queue:
            index = queue.pop(0)
            visited.append(index)
            for key in rooms[index]:
                if key not in visited and key not in queue:
                    queue.append(key)
        return len(visited) == len(rooms)
            
            
            
        
