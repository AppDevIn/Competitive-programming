
import math
def solve (N):
    # Your code goes here
    n=int(math.sqrt(N))
    for i in range(2,n):
        if N%i==0:
            return 'NO'
    else:
        return 'YES'

T = int(input())
for _ in range(T):
    N = int(input())

    out_ = solve(N)
    print (out_)