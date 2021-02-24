def maxheightrea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l = 0
    r = len(height) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(height[l], 
                        height[r]) * (r - l))
     
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return area



print("🚀 ~ file: containerWithMostWater.py ~ line 15 ~ maxheightrea([1, 8, 6, 2, 5, 4, 8, 3, 7])", maxheightrea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

