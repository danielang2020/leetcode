from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ To go from O(n²) → O(n), you use extra space to store intermediate results or avoid recomputation.

        Args:
            nums (List[int]): _description_
            target (int): _description_

        Returns:
            List[int]: _description_
        """        
        map = {}
        for i in range(len(nums)):
            n = nums[i]
            want = target - n
            if want in map:
                return [i, map[want]]
            map[n] = i


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_twoSum(self):
        self.assertListEqual(
            sorted(self.instance.twoSum([2, 7, 11, 15], 9)), sorted([1, 0])
        )
        self.assertListEqual(sorted(self.instance.twoSum([3, 2, 4], 6)), sorted([2, 1]))
        self.assertListEqual(sorted(self.instance.twoSum([3, 3], 6)), sorted([1, 0]))
        self.assertListEqual(
            sorted(self.instance.twoSum([1, 2, 3, 4, 5], 9)), sorted([4, 3])
        )
        self.assertListEqual(
            sorted(self.instance.twoSum([-1, -2, -3, -4, -5], -8)), sorted([2, 4])
        )


if __name__ == "__main__":
    unittest.main()
