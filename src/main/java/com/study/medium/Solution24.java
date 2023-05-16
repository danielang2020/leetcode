package com.study.medium;

/**
 * @see <a href="https://leetcode.com/problems/swap-nodes-in-pairs/">Swap Nodes in Pairs</a>
 * @program: leetcode
 * @author: Daniel
 * @create: 2023-05-16 20:24
 **/
public class Solution24 {
	public static void main(String[] args) {
		ListNode n4 = new ListNode(4, null);
		ListNode n3 = new ListNode(3, n4);
		ListNode n2 = new ListNode(2, n3);
		ListNode n1 = new ListNode(1, n2);

		System.out.println(n1);

		Solution24 solution24 = new Solution24();
		ListNode listNode = solution24.swapPairs(n1);

		System.out.println(listNode);
	}

	public ListNode swapPairs(ListNode head) {
		if ((head == null) || (head.next == null)) {
			return head;
		}

		ListNode first = head;
		ListNode second = head.next;

		first.next = swapPairs(second.next);
		second.next = first;

		return second;
	}
}


class ListNode {
	int val;
	ListNode next;

	ListNode() {
	}

	ListNode(int val) {
		this.val = val;
	}

	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}

	@Override
	public String toString() {
		return "{" + "val=" + val + ", next=" + next + '}';
	}
}