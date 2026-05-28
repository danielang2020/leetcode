from typing import List
import unittest
# sorted list means increasing will be larger and decreasing will be smaller.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            x = numbers[left]
            y = numbers[right]
            s = x + y
            if s == target:
                return [left+1,right+1]
            elif s < target:
                left +=1
            else:
                right-=1
        
                    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_twoSum1(self):
        result = self.instance.twoSum([2,7,11,15], 9)

        self.assertEqual(result, [1,2])
        
    def test_twoSum2(self):
        result = self.instance.twoSum([2,3,4], 6)

        self.assertEqual(result, [1,3])
        
    def test_twoSum3(self):
        result = self.instance.twoSum([-1,0], -1)

        self.assertEqual(result, [1,2])            
            
             
            


if __name__ == "__main__":
    unittest.main()