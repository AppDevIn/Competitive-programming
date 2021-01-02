
def solution(chocolates, M, N):
    
    arr = [0]*M # Generate M number of boxes
    max_sum = total = 0
    
    # Loop through the person to get the choclatess
    for n in chocolates:
    
        total += n #Add the choclate to total
        leftOver = total % M 
    
        if leftOver == 0:
            max_sum = max(max_sum, total)
        elif arr[leftOver] == 0:
             arr[leftOver] = total
        else:
            max_sum = max(max_sum, total - arr[leftOver])
    
    return str(max_sum // M)
 

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    chocolates = list(map(int, input().split()))

    out_ = solution(chocolates, M, N)
    print(out_)