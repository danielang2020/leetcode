package com.study.easy;

import java.util.HashMap;
import java.util.Map;

/**
 * @see <a href="https://leetcode.com/problems/two-sum/">Two Sum</a>
 * @program: leetcode
 * @author: Daniel
 * @create: 2023-05-17 21:25
 **/
public class Solution1 {
	public static void main(String[] args) {
		int[] nums = {3, 2, 4};
		int target = 6;

		Solution1 solution1 = new Solution1();

		System.out.println("" + solution1.twoSum(nums, target)[0] + solution1.twoSum(nums, target)[1]);
	}


	public int[] twoSum1(int[] nums, int target) {
		for (int i = 0; i < nums.length; i++) {
			for (int n = i + 1; n < nums.length; n++) {
				int r = nums[i] + nums[n];
				if (r == target) {
					return new int[]{i, n};
				}
			}
		}
		return null;
	}

	public int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> cache = new HashMap<>(nums.length);

		for (int i = 0; i < nums.length; i++) {
			int left = target - nums[i];
			if (cache.containsKey(left) && cache.get(left) != i) {
				return new int[]{i, cache.get(left)};
			} else {
				cache.put(nums[i], i);
			}
		}

		return null;
	}
}
