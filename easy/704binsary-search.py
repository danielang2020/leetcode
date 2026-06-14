from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1
        
        while(low <= high):
            mid = (low + high) >> 1
            temp = nums[mid]
            if(temp == target):
                return mid
            elif(temp > target):
                high = mid - 1
            else:
                low = mid + 1
            
        return -1
                
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_search(self):
        self.assertEqual(self.instance.search([-1,0,3,5,9,12],9),4)
        self.assertEqual(self.instance.search([-1,0,3,5,9,12],2),-1)


if __name__ == "__main__":
    unittest.main()