package com.study.easy;

/**
 * @see <a href="https://leetcode.com/problems/palindrome-number/">Palindrome Number</a>
 * @program: leetcode
 * @author: Daniel
 * @create: 2023-05-21 16:35
 **/
public class Solution9 {

	public static void main(String[] args) {
		System.out.println(new Solution9().isPalindrome(0));
	}

	public boolean isPalindrome(int x) {
		if (x < 0 || (x % 10 == 0 && x != 0)) {
			return false;
		}

		int reversedNum = 0;

		while (x > reversedNum) {
			reversedNum = reversedNum * 10 + x % 10;
			x /= 10;
		}

		return x == reversedNum || reversedNum / 10 == x;
	}
}
