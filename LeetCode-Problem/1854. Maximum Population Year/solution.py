class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        l = []
        for birth, death in logs:
            l.append((birth,1))
            l.append((death,0))
        
        l.sort(key=lambda x: (x[0], x[1] == 1))

        maximumPopulation = -1
        population = 0
        maxYear = -1

        for year, status in l:
            if not status:
                population -= 1
            else:
                 population += 1
            if population > maximumPopulation:
                maximumPopulation = population
                maxYear = year
        
        return maxYear

        
