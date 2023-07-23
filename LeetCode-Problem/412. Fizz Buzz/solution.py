class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for x in range(n):
            ans = ""
            if (x + 1) % 3 == 0:
                ans += "Fizz"
            if (x + 1) % 5 == 0:
                ans += "Buzz"

            answer.append(ans if ans != "" else str(x+1))
        return answer

