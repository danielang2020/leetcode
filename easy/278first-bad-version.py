# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import unittest

class Solution:
    def isBadVersion(self,version: int) -> bool:
        return version >= 3
        
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = (high + low) // 2
            bad = self.isBadVersion(mid)
            if bad:
                high = mid # keep the mid as high, so we can use "while low < high" instead of "while low <= high"
            else:
                low = mid + 1
        return low
                
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_search(self):
        self.assertEqual(self.instance.firstBadVersion(5),3)


if __name__ == "__main__":
    unittest.main()