from Average_of_Levels_in_Binary_Tree import Solution, TreeNode
import pytest


@pytest.fixture
def start():
    return Solution()

def testCase01(start:Solution):
    assert start.averageOfLevels(TreeNode(5, TreeNode(2), TreeNode(-3))) == [5.00000,-0.50000]

def testCase02(start:Solution):
    assert start.averageOfLevels(TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))) == [3.00000,14.50000,11.00000]

