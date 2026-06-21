from typing import List
import unittest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2 
            
            if nums[mid] == target:
                start = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2 
            
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return [start,end]
        
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_search(self):
        self.assertListEqual(self.instance.searchRange([5,7,7,8,8,10],8),[3,4])
        self.assertListEqual(self.instance.searchRange([5,7,7,8,8,10],6),[-1,-1])
        self.assertListEqual(self.instance.searchRange([],0),[-1,-1])
        self.assertListEqual(self.instance.searchRange([1],1),[0,0])
        self.assertListEqual(self.instance.searchRange([2,2],2),[0,1])


if __name__ == "__main__":
    unittest.main()