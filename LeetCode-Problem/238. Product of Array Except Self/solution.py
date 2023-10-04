class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1]*nums[i])
        
        for i in range(len(nums)-1, -1, -1):
            
            if i == len(nums)-1:
                postfix.insert(0, nums[i])
            else:
                postfix.insert(0, postfix[0]*nums[i])
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(1*postfix[1])
            elif i == len(nums)-1:
                output.append(1*prefix[-2])
                break
            else:
                output.append(prefix[i-1]*postfix[i+1])
            
        return output

        

    
