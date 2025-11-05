from typing import List
import unittest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map = {}
       idx = 0
       for n in nums:
           want = target - n
           if want in map:
               return [idx,map[want]]
           map[n] = idx 
           idx+=1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()
        
    def test_twoSum(self):
        self.assertListEqual(sorted(self.instance.twoSum([2,7,11,15], 9)), sorted([1,0]))
        self.assertListEqual(sorted(self.instance.twoSum([3,2,4], 6)), sorted([2,1]))
        self.assertListEqual(sorted(self.instance.twoSum([3,3], 6)), sorted([1,0]))
        self.assertListEqual(sorted(self.instance.twoSum([1,2,3,4,5], 9)), sorted([4,3]))
        self.assertListEqual(sorted(self.instance.twoSum([-1,-2,-3,-4,-5], -8)), sorted([2,4]))
        
if __name__ == "__main__":
    unittest.main()