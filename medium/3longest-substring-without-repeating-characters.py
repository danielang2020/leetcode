import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        charSet = set()
        
        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
                
        return maxLength

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.instance = Solution()

    def test_lengthOfLongestSubstring1(self):
        result = self.instance.lengthOfLongestSubstring("abcabcbb")

        self.assertEqual(result, 3)
        
    def test_lengthOfLongestSubstring2(self):
        result = self.instance.lengthOfLongestSubstring("bbbbb")

        self.assertEqual(result, 1)
        
    def test_lengthOfLongestSubstring3(self):
        result = self.instance.lengthOfLongestSubstring("pwwkew")

        self.assertEqual(result, 3)

     


if __name__ == "__main__":
    unittest.main()
