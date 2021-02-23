def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
    curr = nums[0] + 10
    removedValue = 0
    for x in range(len(nums)):
        x = x - removedValue
        if nums[x] != curr:
            curr = nums[x]
        else: 
            removedValue += 1
            del nums[x]

   
    return len(nums)

removeDuplicates([1,1,2])