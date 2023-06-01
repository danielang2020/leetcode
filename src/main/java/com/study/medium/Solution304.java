package com.study.medium;

/**
 * @see <a href="https://leetcode.com/problems/range-sum-query-2d-immutable/">Range Sum Query 2D - Immutable</a>
 * @program: leetcode
 * @author: Daniel
 * @create: 2023-06-01 10:06
 **/
public class Solution304 {
	private int[][] dp;

	private String[][] dpf;

	public Solution304(int[][] matrix) {
		if (matrix.length == 0 || matrix[0].length == 0) return;
		dp = new int[matrix.length + 1][matrix[0].length + 1];
		dpf = new String[matrix.length + 1][matrix[0].length + 1];
		for (int r = 0; r < matrix.length; r++) {
			for (int c = 0; c < matrix[0].length; c++) {
				System.out.print(matrix[r][c] + " ");
				dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] + matrix[r][c] - dp[r][c];
				dpf[r + 1][c + 1]= dp[r + 1][c] + " + " + dp[r][c + 1] + " + " +  matrix[r][c] + " - " + dp[r][c];
			}
			System.out.println();
		}
		System.out.println();
		for (int r = 0; r < matrix.length; r++) {
			for (int c = 0; c < matrix[0].length; c++) {
				System.out.print(dp[r][c] + "=" + dpf[r][c] + " ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		int[][] m = {{3, 0, 1, 4, 2}, {5, 6, 3, 2, 1}, {1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}};
		Solution304 solution304 = new Solution304(m);
		int sum = solution304.sumRegion(0,0,4,4);
		System.out.println(sum);
	}

	public int sumRegion(int row1, int col1, int row2, int col2) {
		return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1];
	}
}
