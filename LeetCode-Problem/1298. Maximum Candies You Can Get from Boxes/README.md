# [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03)

You have <code>n</code> boxes labeled from <code>0</code> to <code>n - 1</code>. You are given four arrays: <code>status</code>, <code>candies</code>, <code>keys</code>, and <code>containedBoxes</code> where:

- <code>status[i]</code> is <code>1</code> if the <code>i^th</code> box is open and <code>0</code> if the <code>i^th</code> box is closed,
- <code>candies[i]</code> is the number of candies in the <code>i^th</code> box,
- <code>keys[i]</code> is a list of the labels of the boxes you can open after opening the <code>i^th</code> box.
- <code>containedBoxes[i]</code> is a list of the boxes you found inside the <code>i^th</code> box.

You are given an integer array <code>initialBoxes</code> that contains the labels of the boxes you initially have. You can take all the candies in **any open box**  and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

**Example 1:** 

```
Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
```

**Example 2:** 

```
Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.
```

**Constraints:** 

- <code>n == status.length == candies.length == keys.length == containedBoxes.length</code>
- <code>1 <= n <= 1000</code>
- <code>status[i]</code> is either <code>0</code> or <code>1</code>.
- <code>1 <= candies[i] <= 1000</code>
- <code>0 <= keys[i].length <= n</code>
- <code>0 <= keys[i][j] < n</code>
- All values of <code>keys[i]</code> are **unique** .
- <code>0 <= containedBoxes[i].length <= n</code>
- <code>0 <= containedBoxes[i][j] < n</code>
- All values of <code>containedBoxes[i]</code> are unique.
- Each box is contained in one box at most.
- <code>0 <= initialBoxes.length <= n</code>
- <code>0 <= initialBoxes[i] < n</code>
