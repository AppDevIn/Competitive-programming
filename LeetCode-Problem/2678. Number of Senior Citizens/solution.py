class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for d in details:
            age = int(d[11]+d[12])
            if age > 60:
                count += 1
        return count 

